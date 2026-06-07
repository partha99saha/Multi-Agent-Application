from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)


def create_chunks(text: str):

    chunks = splitter.split_text(text)

    return chunks


if __name__ == "__main__":

    sample_text = """
    Python is a powerful programming language.
    It is used in AI, ML, Data Science,
    Web Development and Automation.
    """ * 100

    chunks = create_chunks(sample_text)

    print(f"Total Chunks: {len(chunks)}")

    print("\nFirst Chunk:\n")
    print(chunks[0])
