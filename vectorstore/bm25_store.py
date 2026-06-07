from rank_bm25 import BM25Okapi
import os
import json

# in-memory store (simple version)
_documents = []
_tokenized_corpus = []
bm25 = None


def build_bm25(documents):
    """
    documents = list of Qdrant-like points
    """

    global bm25, _documents, _tokenized_corpus

    _documents = documents

    corpus = [doc.payload["text"] for doc in documents if "text" in doc.payload]

    _tokenized_corpus = [doc.lower().split() for doc in corpus]

    bm25 = BM25Okapi(_tokenized_corpus)

    print("BM25 index built")


def bm25_search(query, k=5):

    if bm25 is None:
        return []

    tokenized_query = query.lower().split()

    scores = bm25.get_scores(tokenized_query)

    ranked = sorted(zip(_documents, scores), key=lambda x: x[1], reverse=True)

    return [doc for doc, score in ranked[:k]]
