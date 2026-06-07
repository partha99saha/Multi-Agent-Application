from vectorstore.retriever import search_documents
from vectorstore.reranker import rerank
from backend.llm import ask_llm
from evaluation.rag_evaluator import evaluate_rag


def rag_node(state):

    question = state["question"]

    # Step 1: retrieve
    docs = search_documents(question, limit=20)

    # Step 2: rerank
    docs = rerank(question, docs)[:5]

    # Step 3: build context
    context = "\n\n".join([d.payload["text"] for d in docs])

    prompt = f"""
            You are a helpful assistant.

            Use ONLY the context below.

            If answer is not present, say:
            "I don't have enough information in the documents."

            Context:
            {context}

            Question:
            {question}
        """

    answer = ask_llm(prompt)

    return {
        "question": question,
        "answer": answer,
        "documents": [
            {"source": d.payload.get("source"), "chunk_id": d.payload.get("chunk_id")}
            for d in docs
        ],
    }
