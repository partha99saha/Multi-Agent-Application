from vectorstore.retriever import search_documents
from backend.llm import ask_llm


def ask_rag(question: str):
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

        prompt = f"""
        You are a helpful assistant.

        If the answer is not present in the context,
        say:

        'I could not find that information in the documents.'

        Documents:
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
