def optimize_context(question: str, context):
    """
    Reduce token usage by trimming and focusing context
    """

    if not context:
        return question

    # if context is list (RAG output)
    if isinstance(context, dict) and "sources" in context:
        sources = context["sources"][:3]  # top 3 only

        text = "\n".join([s["text"][:300] for s in sources])

        return f"""
        Question: {question}

        Context:
        {text}
        """

    return question
