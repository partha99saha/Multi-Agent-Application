from fastapi import FastAPI
from backend.llm import ask_llm
from backend.rag import ask_rag

app = FastAPI()
# uvicorn backend.main:app --reload
# uvicorn backend.main:app --log-level debug


@app.get("/")
def home():
    return {"message": "LLM Engineering Project Started"}


@app.get("/ask")
def ask(question: str):

    answer = ask_llm(question)

    return {"question": question, "answer": answer}


@app.get("/rag")
def rag(question: str):

    result = ask_rag(question)

    return {
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"],
    }
