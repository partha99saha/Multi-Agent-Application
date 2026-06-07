from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision

from datasets import Dataset


def evaluate_rag(question, answer, contexts):

    data = {
        "question": [question],
        "answer": [answer],
        "contexts": [contexts],
    }

    dataset = Dataset.from_dict(data)

    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision],
    )

    return result.to_pandas().to_dict()
