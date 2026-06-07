from vectorstore.embedding import create_embedding
from vectorstore.qdrant_store import client, COLLECTION_NAME


def search_documents(query_text: str, limit: int = 5):
    query_embedding = create_embedding(query_text)

    results = client.query_points(
        collection_name=COLLECTION_NAME, query=query_embedding, limit=limit
    )

    return results.points


if __name__ == "__main__":

    hits = search_documents("What is EC2?")
    hits = search_documents("What is Azure Functions?")
    hits = search_documents("What is scalability?")

    print(f"\nResults Found: {len(hits)}\n")

    for i, hit in enumerate(hits, start=1):
        print(f"\nResult {i}")
        print("-" * 50)
        print(hit.payload)
        print("\nSOURCE:")
        # print(hit.payload["source"])

        print("\nCHUNK:")
        print(hit.payload["chunk_id"])

        print("\nTEXT:")
        print(hit.payload["text"][:300])
