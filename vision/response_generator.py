"""Generate simple text responses in various styles."""

from typing import Any


def generate_response(context: Any, style: str) -> str:
    """Return a short message using the desired style.

    This is placeholder logic that can later be replaced with
    a real OpenAI call.
    """
    if not isinstance(context, str):
        context = str(context)
    if not isinstance(style, str):
        style = str(style)
    return f"This is a {style} style message for context: {context}"

