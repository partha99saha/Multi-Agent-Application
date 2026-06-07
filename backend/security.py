def detect_prompt_injection(text: str) -> bool:
    suspicious_patterns = [
        "ignore previous instructions",
        "reveal system prompt",
        "you are now",
        "act as system",
        "disregard above",
    ]

    text_lower = text.lower()

    return any(p in text_lower for p in suspicious_patterns)
