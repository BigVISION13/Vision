from dataclasses import dataclass, field
from typing import Any, Dict, List

from .workflow import parse_workflow

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
    """Generate a simple automation flow from a natural language prompt."""
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
