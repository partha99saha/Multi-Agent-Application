from uuid import uuid4

from ingestion.pdf_loader import load_pdf
from ingestion.chunker import create_chunks

from vectorstore.embedding import create_embedding
from vectorstore.qdrant_store import client, COLLECTION_NAME

from qdrant_client.models import PointStruct


def ingest_pdf(pdf_path: str):

    print("Loading PDF...")

    text = load_pdf(pdf_path)

    print("Creating Chunks...")

    chunks = create_chunks(text)

    print(f"Total Chunks: {len(chunks)}")

    points = []

    for idx, chunk in enumerate(chunks):

        embedding = create_embedding(chunk)

        points.append(
            PointStruct(
                id=str(uuid4()),
                vector=embedding,
                payload={
                    "text": chunk,
                    "source": pdf_path,
                    "document_id": pdf_path,
                    "chunk_id": idx,
                },
            )
        )

    print("Uploading to Qdrant...")

    client.upsert(collection_name=COLLECTION_NAME, points=points)

    print("Upload Complete")


if __name__ == "__main__":

    ingest_pdf("data/system_design.pdf")
    ingest_pdf("data/aws.pdf")
    ingest_pdf("data/azure.pdf")
