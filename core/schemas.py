from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class ToolCall(BaseModel):
    name: str
    input: str


class AgentState(BaseModel):
    question: str
    route: Optional[str] = None

    plan: Optional[List[str]] = None

    context: Optional[str] = None
    retrieved_docs: Optional[List[Dict[str, Any]]] = None

    answer: Optional[str] = None
    final_answer: Optional[str] = None

    tool_calls: Optional[List[ToolCall]] = []
