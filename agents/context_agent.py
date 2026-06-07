def context_node(state):

    docs = state["documents"]

    context = "\n\n".join([d.payload["text"] for d in docs])

    return {"context": context}
