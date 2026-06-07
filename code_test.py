from vectorstore.hybrid_retriever import hybrid_search

results = hybrid_search("what is ec2", 5)

for r in results:
    print(r.payload["text"][:200])
