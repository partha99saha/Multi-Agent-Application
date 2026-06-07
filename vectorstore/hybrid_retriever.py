from vectorstore.retriever import search_documents
from vectorstore.bm25_store import bm25_search


def hybrid_search(query, limit=10):

    from llm.query_rewriter import rewrite_query

    rewritten_query = rewrite_query(query)
    vector_results = search_documents(rewritten_query, limit=limit)
    bm25_results = bm25_search(rewritten_query, k=limit)

    # merge (simple dedup)
    seen = set()
    merged = []

    for r in vector_results + bm25_results:
        text = r.payload["text"]

        if text not in seen:
            seen.add(text)
            merged.append(r)

    return merged[:limit]
