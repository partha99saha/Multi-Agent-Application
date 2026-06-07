# tools/llm_tool.py

from tools.tool_registry import register_tool
from backend.llm import ask_llm


@register_tool("llm")
def llm_tool(query: str):
    return ask_llm(query)
