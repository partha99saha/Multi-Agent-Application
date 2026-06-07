from vectorstore.retriever import search_documents
from backend.llm import ask_llm
from utils.timer import timeit
from backend.security import detect_prompt_injection


@timeit("rag_pipeline")
def ask_rag(question: str):
    if detect_prompt_injection(question):
        return {
            "answer": "I cannot assist with that request.",
            "sources": [],
        }

    try:
        from vectorstore.reranker import rerank

        results = search_documents(question, limit=20)

        results = rerank(question, results)[:5]

        sources = []

        for result in results:

            sources.append(
                {
                    "source": result.payload.get("source"),
                    "chunk_id": result.payload.get("chunk_id"),
                    "text": result.payload["text"],
                }
            )

        context = "\n\n".join([source["text"] for source in sources])
        if not context:
            return {"answer": "No relevant context found", "sources": []}

        prompt = f"""
        You are a helpful technical assistant.

        Use ONLY the context below.

        IMPORTANT RULES:
        - "Azure Function App" and "Azure Functions" refer to the same concept.
        - If the context contains semantically similar information, treat it as valid.
        - Do NOT say you cannot find the answer if context is relevant.
        - Always try to infer meaning from provided context.

        If the answer is not truly present, then say:
        "I could not find that information in the documents."

        Context:
        {context}

        Question:
        {question}
        """

        answer = ask_llm(prompt)

        return {"answer": answer, "sources": sources}
    except Exception as e:
        print(f"Error in ask_rag: {e}")
        return {
            "answer": "An error occurred while processing your request.",
            "sources": [],
        }


if __name__ == "__main__":

    question = input("Question: ")

    response = ask_rag(question)

    print("\nAnswer:\n")

    print(response)
