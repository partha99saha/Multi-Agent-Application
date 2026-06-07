from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)


def create_chunks(text: str, metadata: dict = None):

    chunks = splitter.split_text(text)

    results = []

    for i, chunk in enumerate(chunks):
        results.append({"text": chunk, "chunk_id": i, "metadata": metadata or {}})

    return results
