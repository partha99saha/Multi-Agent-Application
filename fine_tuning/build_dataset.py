import os
import json
from vectorstore.retriever import search_documents

DATA_PATH = "data"
OUTPUT_FILE = "fine_tuning/dataset.jsonl"


def get_queries():
    """
    You can expand this list later.
    Keep it domain-focused.
    """

    return [
        "What is EC2?",
        "What is AWS Lambda?",
        "What is VPC?",
        "What is Azure resource group?",
        "What is system design scalability?",
        "What is load balancing?",
        "What is Docker container?",
        "What is Kubernetes?",
    ]


def build_dataset():

    os.makedirs("fine_tuning", exist_ok=True)

    queries = get_queries()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        for q in queries:

            print(f"Processing: {q}")

            results = search_documents(q, limit=3)

            for r in results:

                text = r.payload.get("text", "")

                if not text:
                    continue

                record = {"query": q, "positive": text}

                f.write(json.dumps(record) + "\n")

    print(f"Dataset created at {OUTPUT_FILE}")


if __name__ == "__main__":
    build_dataset()
