import uuid
from ingestion.loaders import load_document
from ingestion.chunker import create_chunks
from vectorstore.embedding import create_embedding
from vectorstore.qdrant_store import client, COLLECTION_NAME


def ingest_file(file_path: str):

    text = load_document(file_path)

    chunks = create_chunks(text, metadata={"source": file_path})

    points = []

    for c in chunks:

        vector = create_embedding(c["text"])

        points.append(
            {
                "id": str(uuid.uuid4()),
                "vector": vector,
                "payload": {
                    "text": c["text"],
                    "chunk_id": c["chunk_id"],
                    "source": file_path,
                },
            }
        )

    client.upsert(collection_name=COLLECTION_NAME, points=points)

    return {"file": file_path, "chunks_indexed": len(points)}
