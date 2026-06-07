from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")





vector = embeddings.embed_query(
    "What is EC2?"
)

print(len(vector))