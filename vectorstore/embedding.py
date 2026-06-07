from sentence_transformers import SentenceTransformer

_model = None


def get_model():
    global _model

    if _model is None:
        print("Loading embedding model...")
        # _model = SentenceTransformer("BAAI/bge-small-en-v1.5")
        _model = SentenceTransformer("fine_tuned_embedding_model")
        print("Model loaded")

    return _model


def create_embedding(text: str):
    try:
        model = get_model()
        embedding = model.encode(text)

        return embedding.tolist()
    except Exception as e:
        print(f"Error creating embedding: {e}")
        return None
