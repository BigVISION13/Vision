import json


def parse_workflow(prompt: str) -> dict:
    """Parse a natural language prompt into a structured workflow.

    The current implementation extracts LinkedIn connection requests,
    waiting periods, email actions, and conditional follow-ups.
    """
    if not isinstance(prompt, str):
        prompt = str(prompt)

    text = prompt.strip().lower()
    workflow = {"sequence": []}

    # Find target and LinkedIn connection request
    if "target" in text and "connection request on linkedin" in text:
        start = text.find("target") + 6
        end = text.find(", send a connection request on linkedin")
        target = text[start:end].strip()
        workflow["sequence"].append({
            "action": "send_linkedin_request",
            "target": target
        })

    # Find "wait X days then send a Y email"
    if "wait" in text and "then send" in text and "email" in text:
        try:
            start = text.find("wait") + 4
            end = text.find("days", start)
            days = int(text[start:end].strip())
            temp = text[end + 4:text.find("email", end)].replace("then send", "").strip()
            template = temp if temp else "custom"
            workflow["sequence"].append({"action": "wait", "duration_days": days})
            workflow["sequence"].append({"action": "send_email", "template": template.replace("a ", "").replace(" ", "_") + "_email"})
        except Exception:
            pass  # If the pattern is not matched, just skip

    # Find conditional email follow-up
    if "if no reply after" in text and "send" in text and "email" in text:
        try:
            start = text.find("if no reply after") + 17
            end = text.find("days", start)
            days = int(text[start:end].strip())
            start2 = text.find("send", end) + 4
            end2 = text.find("email", start2)
            template = text[start2:end2].replace("a", "").strip()
            if not template:
                template = "follow-up"
            workflow["sequence"].append({
                "action": "conditional",
                "condition": "no_reply",
                "wait_days": days,
                "true_branch": [
                    {"action": "send_email", "template": template.replace(" ", "_") + "_email"}
                ],
                "false_branch": []
            })
        except Exception:
            pass

    return workflow


if __name__ == "__main__":
    sample_input = (
        "Target Workday finance directors at mid-market firms, send a connection request on LinkedIn. "
        "Wait 2 days then send a custom email. If no reply after 3 days, send a follow-up email."
    )
    parsed = parse_workflow(sample_input)
    print(json.dumps(parsed, indent=2))
