from langgraph.graph import StateGraph, END

from agents.state import GraphState
from agents.planner import planner
from agents.retriever_agent import retriever_node
from agents.reranker_agent import reranker_node
from agents.context_agent import context_node
from agents.answer_agent import answer_node
from agents.critic_agent import critic_node


def direct_node(state):

    return {"final_answer": "Direct LLM path (not using RAG)"}


workflow = StateGraph(GraphState)

workflow.add_node("planner", planner)
workflow.add_node("retriever", retriever_node)
workflow.add_node("reranker", reranker_node)
workflow.add_node("context", context_node)
workflow.add_node("answer", answer_node)
workflow.add_node("critic", critic_node)
workflow.add_node("direct", direct_node)


def route(state):
    return state.route


workflow.add_conditional_edges(
    "planner", route, {"rag": "retriever", "direct": "direct"}
)

workflow.add_edge("retriever", "reranker")
workflow.add_edge("reranker", "context")
workflow.add_edge("context", "answer")
workflow.add_edge("answer", "critic")

workflow.add_edge("critic", END)
workflow.add_edge("direct", END)

workflow.set_entry_point("planner")

app = workflow.compile()
