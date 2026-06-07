import re

PATTERNS = [
    r"ignore (all|previous|any) instructions",
    r"forget (all|previous) context",
    r"disregard (all|above|previous)",
    r"you are now (a|an)?",
    r"act as (system|developer|admin|root)",
    r"switch (to)? (developer|debug|jailbreak) mode",
    r"reveal (system|hidden|developer) prompt",
    r"print (your|the) instructions",
    r"bypass (filters|restrictions|safety)",
]


def detect_prompt_injection(text: str) -> bool:
    text = text.lower()

    return any(re.search(p, text) for p in PATTERNS)
