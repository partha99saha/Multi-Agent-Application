# tools/rag_tool.py

from tools.tool_registry import register_tool
from backend.rag import ask_rag


@register_tool("rag")
def rag_tool(query: str):
    return ask_rag(query)
