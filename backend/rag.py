from vectorstore.retriever import search_documents
from backend.llm import ask_llm
from utils.timer import timeit
from backend.security import detect_prompt_injection
from backend.session_manager import is_cancelled


@timeit("rag_pipeline")
def ask_rag(question, session_id=None, task_id=None):

    # ---------------------------
    # CANCEL CHECK (EARLY EXIT)
    # ---------------------------
    if session_id and task_id and is_cancelled(session_id, task_id):
        return {"answer": "Cancelled", "sources": []}

    # ---------------------------
    # PROMPT INJECTION SAFETY
    # ---------------------------
    if detect_prompt_injection(question):
        return {
            "answer": "I cannot assist with that request.",
            "sources": [],
        }

    try:
        from vectorstore.reranker import rerank

        # ---------------------------
        # RETRIEVAL
        # ---------------------------
        results = search_documents(question, limit=20)

        if session_id and task_id and is_cancelled(session_id, task_id):
            return {"answer": "Cancelled", "sources": []}

        # ---------------------------
        # RERANKING
        # ---------------------------
        results = rerank(question, results)[:5]

        if session_id and task_id and is_cancelled(session_id, task_id):
            return {"answer": "Cancelled", "sources": []}

        # ---------------------------
        # BUILD SOURCES
        # ---------------------------
        sources = []
        for result in results:
            sources.append(
                {
                    "source": result.payload.get("source"),
                    "chunk_id": result.payload.get("chunk_id"),
                    "text": result.payload.get("text", ""),
                }
            )

        context = "\n\n".join([s["text"] for s in sources])

        if not context.strip():
            return {"answer": "No relevant context found", "sources": []}

        # ---------------------------
        # FINAL CANCEL CHECK BEFORE LLM
        # ---------------------------
        if session_id and task_id and is_cancelled(session_id, task_id):
            return {"answer": "Cancelled", "sources": []}

        # ---------------------------
        # PROMPT
        # ---------------------------
        prompt = f"""
            You are a helpful technical assistant.

            Use ONLY the context below.

            IMPORTANT RULES:
            - "Azure Function App" and "Azure Functions" refer to the same concept.
            - Do NOT hallucinate outside context.
            - If context is relevant, infer intelligently.
            - If not present, say: "I could not find that information in the documents."

            Context:
            {context}

            Question:
            {question}
            """

        # ---------------------------
        # LLM CALL
        # ---------------------------
        answer = ask_llm(prompt, session_id=session_id, task_id=task_id)

        return {
            "answer": answer,
            "sources": sources,
        }

    except Exception as e:
        print(f"Error in ask_rag: {e}")
        return {
            "answer": "An error occurred while processing your request.",
            "sources": [],
        }


# ---------------------------
# LOCAL TEST
# ---------------------------
if __name__ == "__main__":
    q = input("Question: ")
    print(ask_rag(q))
