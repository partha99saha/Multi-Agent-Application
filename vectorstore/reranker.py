from sentence_transformers import CrossEncoder
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN", "")

_model = None


def get_reranker():
    global _model

    if _model is None:
        print("Loading reranker model...")

        _model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

        print("Reranker loaded")

    return _model


def rerank(question, results):
    """
    Re-ranks Qdrant search results using CrossEncoder.

    Args:
        question (str)
        results (list): Qdrant search results (points)

    Returns:
        list: reranked results (best first)
    """

    model = get_reranker()

    pairs = [(question, r.payload["text"]) for r in results if "text" in r.payload]

    if not pairs:
        return results

    scores = model.predict(pairs)

    ranked = sorted(zip(results, scores), key=lambda x: x[1], reverse=True)

    return [item[0] for item in ranked]
