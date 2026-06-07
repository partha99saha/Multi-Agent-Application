from tools.tool_registry import get_tool


def route_question(question: str) -> str:
    q = question.lower()

    # simple heuristic routing
    if any(word in q for word in ["what is", "explain", "define", "how does"]):
        return "rag"

    return "llm"


def execute(question: str):
    tool_name = route_question(question)
    tool = get_tool(tool_name)

    if not tool:
        return {"error": "No tool found"}

    return tool(question)
