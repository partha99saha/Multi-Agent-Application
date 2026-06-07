from backend.llm import ask_llm

from evaluation.confidence import compute_confidence


def answer_node(state):

    question = state.question
    context = state.context

    answer = ask_llm(f"""
        Use context to answer:

        Context:
        {context}

        Question:
        {question}
        """)

    evaluation = evaluate_rag(question, answer, [context])
    confidence = compute_confidence(evaluation)
    return {"draft_answer": answer, "evaluation": evaluation, "confidence": confidence}
