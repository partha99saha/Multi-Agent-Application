from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(host="localhost", port=6333)

COLLECTION_NAME = "documents"


def create_collection():

    collections = client.get_collections()

    existing = [c.name for c in collections.collections]

    if COLLECTION_NAME not in existing:

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE),
        )

        print("Collection Created")

    else:

        print("Collection Already Exists")


if __name__ == "__main__":
    create_collection()
