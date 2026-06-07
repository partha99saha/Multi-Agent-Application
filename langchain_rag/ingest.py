from langchain_rag.loaders import load_pdf
from langchain_rag.splitter import split_documents

from langchain_rag.vectorstore import get_vectorstore

docs = load_pdf("data/aws.pdf")

chunks = split_documents(docs)

vectorstore = get_vectorstore()

vectorstore.add_documents(chunks)

print(f"Inserted {len(chunks)} chunks")
