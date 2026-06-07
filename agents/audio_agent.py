from tools.tool_registry import get_tool


def audio_node(state):

    tool = get_tool("tts")

    result = tool(state["question"])

    return {"final_answer": result}
