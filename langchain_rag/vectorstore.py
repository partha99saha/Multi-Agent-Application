from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

from langchain_qdrant import QdrantVectorStore
from langchain_rag.embeddings import embeddings

client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "langchain_docs"


def init_collection():
    """Create collection if it doesn't exist"""

    collections = client.get_collections().collections
    existing = [c.name for c in collections]

    if COLLECTION_NAME not in existing:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

        print("Collection created:", COLLECTION_NAME)


def get_vectorstore():

    init_collection()

    return QdrantVectorStore(
        client=client,
        collection_name=COLLECTION_NAME,
        embedding=embeddings,
    )
