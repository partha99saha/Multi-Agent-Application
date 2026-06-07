from tools.tool_registry import get_tool


def image_node(state):

    tool = get_tool("image")

    result = tool(state["question"])

    return {"final_answer": result}
