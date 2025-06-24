import json
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List

from .workflow import parse_workflow

try:  # optional OpenAI integration for richer automations
    import openai  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    openai = None  # type: ignore

@dataclass
class Node:
    action: str
    params: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Flow:
    nodes: List[Node] = field(default_factory=list)
    connections: List[Dict[str, int]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "nodes": [
                {"id": i, "action": n.action, "params": n.params}
                for i, n in enumerate(self.nodes)
            ],
            "connections": self.connections,
        }

def generate_automation(prompt: str) -> Flow:
    """Generate an automation flow from a natural language prompt.

    If the OpenAI package and an ``OPENAI_API_KEY`` environment variable are
    available, the function will call the ChatGPT API to obtain a richer JSON
    representation of the flow. The expected format is ``{"sequence": [...]}``
    where each element contains an ``action`` field and any parameters. When
    the API is unavailable, it falls back to a simple rule-based parser.
    """

    api_key = os.environ.get("OPENAI_API_KEY")
    if openai and api_key:
        openai.api_key = api_key
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Convert the user's description into a JSON object with a"
                            " 'sequence' list of actions."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
            )
            content = response.choices[0].message.content
            data = json.loads(content)
            workflow = data
        except Exception:
            # On any failure, fall back to the local parser
            workflow = parse_workflow(prompt)
    else:
        workflow = parse_workflow(prompt)

    flow = Flow()
    prev_index = None
    for i, step in enumerate(workflow.get("sequence", [])):
        params = {k: v for k, v in step.items() if k != "action"}
        flow.nodes.append(Node(action=step.get("action", ""), params=params))
        if prev_index is not None:
            flow.connections.append({"from": prev_index, "to": i})
        prev_index = i
    return flow
