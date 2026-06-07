from vectorstore.retriever import search_documents


def retriever_node(state):

    question = state["question"]

    docs = search_documents(question, limit=20)

    return {"documents": docs}
