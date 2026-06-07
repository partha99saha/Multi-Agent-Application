from vectorstore.retriever import search_documents
from backend.rag import ask_rag

dataset = [
    {
        "question": "What is Azure Functions?",
        "keywords": ["serverless", "event-driven"]
    },
    {
        "question": "What is EC2?",
        "keywords": ["compute", "AWS"]
    }
]

def evaluate():
    results = []

    for item in dataset:
        response = ask_rag(item["question"])

        answer = response["answer"].lower()

        score = sum(
            1 for k in item["keywords"] if k.lower() in answer
        )

        results.append({
            "question": item["question"],
            "score": score,
            "answer": response["answer"]
        })

    print(results)

if __name__ == "__main__":
    evaluate()