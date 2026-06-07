from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from langchain_rag.vectorstore import get_vectorstore

llm = ChatOpenAI(model="gpt-4o-mini")

vectorstore = get_vectorstore()
retriever = vectorstore.as_retriever()


# Prompt template
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer ONLY using the context below.
If context is not enough, say:
"I don't have enough information in the documents."

Context:
{context}

Question:
{question}
""")


def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])


# LCEL PIPELINE (modern LangChain)
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
)


if __name__ == "__main__":

    question = input("Question: ")

    result = rag_chain.invoke(question)

    print("\nANSWER:\n")
    print(result.content)
