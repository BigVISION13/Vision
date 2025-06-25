"""Simple heuristics-based sales advice module."""

from typing import Any


def get_sales_advice(prompt: Any) -> str:
    """Return a sales tip based on the provided prompt.

    This function uses very basic keyword matching to simulate
    AI-generated sales advice.
    """
    if not isinstance(prompt, str):
        prompt = str(prompt)

    text = prompt.strip().lower()

    if "cold call" in text:
        return (
            "For successful cold calls, research the prospect and prepare a short, "
            "value-focused opening statement."
        )
    if "closing" in text:
        return (
            "When closing a deal, summarize the agreed benefits and ask for the next "
            "step with confidence."
        )

    return (
        "Always tailor your pitch to the customer's needs and listen carefully to "
        "their objections."
    )
