from vectorstore.retriever import search_documents
from vectorstore.bm25_store import build_bm25


def build_index():

    print("Fetching documents from vector DB...")

    docs = search_documents("init", limit=1000)

    build_bm25(docs)

    print(f"BM25 index built with {len(docs)} docs")


if __name__ == "__main__":
    build_index()
