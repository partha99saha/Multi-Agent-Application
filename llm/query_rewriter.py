from backend.llm import ask_llm


def rewrite_query(question: str) -> str:

    prompt = f"""
        You are an expert search query optimizer.

        Convert the user question into a detailed search query
        for a vector database containing technical documents.

        Rules:
        - Expand abbreviations
        - Add relevant technical keywords
        - Keep it short (1 sentence max)

        Question:
        {question}

        Return only rewritten query.
        """

    return ask_llm(prompt)
