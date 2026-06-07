import json
from vectorstore.retriever import search_documents


def build_triplets():

    queries = [
        "What is EC2?",
        "What is AWS Lambda?",
        "What is VPC?",
        "What is load balancing?",
        "What is system design scalability?",
    ]

    dataset = []

    for q in queries:
        print("Processing:", q)

        results = search_documents(q, limit=5)

        if len(results) < 2:
            continue

        # Top result = positive
        positive = results[0].payload["text"]

        # Lower ranked = negatives
        negatives = [r.payload["text"] for r in results[1:3]]

        dataset.append({"anchor": q, "positive": positive, "negative": negatives})

    with open("fine_tuning/triplets.jsonl", "w", encoding="utf-8") as f:
        for item in dataset:
            f.write(json.dumps(item) + "\n")

    print("Triplet dataset created")


if __name__ == "__main__":
    build_triplets()
