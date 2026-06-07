def safety_check(output):

    if not output:
        return "Unsafe or empty response"

    blocked_phrases = [
        "ignore previous instructions",
        "reveal system prompt",
        "you are now",
        "jailbreak",
    ]

    text = str(output).lower()

    for phrase in blocked_phrases:
        if phrase in text:
            return "Blocked due to unsafe prompt behavior"

    return output
