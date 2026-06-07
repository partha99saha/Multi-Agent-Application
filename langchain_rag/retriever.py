from langchain_rag.vectorstore import get_vectorstore

vectorstore = get_vectorstore()

retriever = vectorstore.as_retriever(search_kwargs={"k": 5})


if __name__ == "__main__":

    docs = retriever.invoke("What is EC2?")

    print("\nRESULTS\n")

    for doc in docs:

        print(doc.metadata)
        print(doc.page_content[:300])
        print("-" * 50)
