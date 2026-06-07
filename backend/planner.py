def create_plan(question: str) -> list:
    """
    Break question into steps (lightweight planner)
    """

    q = question.lower()

    steps = []

    if any(word in q for word in ["what is", "explain", "define"]):
        steps.append("retrieve_context")
        steps.append("generate_answer")

    elif any(word in q for word in ["how", "why"]):
        steps.append("retrieve_context")
        steps.append("analyze_context")
        steps.append("generate_answer")

    else:
        steps.append("direct_answer")

    return steps
