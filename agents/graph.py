from langgraph.graph import StateGraph, END

from agents.state import GraphState
from agents.planner import planner
from agents.retriever_agent import retriever_node
from agents.reranker_agent import reranker_node
from agents.context_agent import context_node
from agents.answer_agent import answer_node
from agents.critic_agent import critic_node

from agents.image_agent import image_node
from agents.audio_agent import audio_node


# ---------------------------
# DIRECT NODE
# ---------------------------
def direct_node(state):

    return {"final_answer": "Direct LLM path (not using RAG)"}


# ---------------------------
# GRAPH
# ---------------------------
workflow = StateGraph(GraphState)

workflow.add_node("planner", planner)

workflow.add_node("retriever", retriever_node)
workflow.add_node("reranker", reranker_node)
workflow.add_node("context", context_node)
workflow.add_node("answer", answer_node)
workflow.add_node("critic", critic_node)

workflow.add_node("direct", direct_node)

workflow.add_node("image", image_node)
workflow.add_node("audio", audio_node)


# ---------------------------
# ROUTING FUNCTION (FIXED)
# ---------------------------
def route(state):
    return state["route"]  # IMPORTANT FIX (dict-style access)


# ---------------------------
# CONDITIONAL ROUTING FROM PLANNER
# ---------------------------
workflow.add_conditional_edges(
    "planner",
    route,
    {"rag": "retriever", "direct": "direct", "image": "image", "audio": "audio"},
)


# ---------------------------
# RAG FLOW
# ---------------------------
workflow.add_edge("retriever", "reranker")
workflow.add_edge("reranker", "context")
workflow.add_edge("context", "answer")
workflow.add_edge("answer", "critic")


# ---------------------------
# END STATES
# ---------------------------
workflow.add_edge("critic", END)
workflow.add_edge("direct", END)
workflow.add_edge("image", END)
workflow.add_edge("audio", END)


# ---------------------------
# ENTRY POINT
# ---------------------------
workflow.set_entry_point("planner")

app = workflow.compile()
