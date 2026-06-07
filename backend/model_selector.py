def select_model(question: str, context=None):

    q = question.lower()

    # simple heuristics (upgrade later to classifier)
    if len(q) < 40:
        return "gpt-4o-mini"

    if any(word in q for word in ["explain", "architecture", "design", "why"]):
        return "gpt-4o"

    if context and len(str(context)) > 2000:
        return "gpt-4o"

    return "gpt-4o-mini"
