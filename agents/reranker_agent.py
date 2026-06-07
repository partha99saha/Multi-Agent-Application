from vectorstore.reranker import rerank


def reranker_node(state):

    question = state["question"]
    docs = state["documents"]

    docs = rerank(question, docs)[:5]

    return {"documents": docs}
