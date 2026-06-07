from fastapi import FastAPI
from backend.router import execute
import tools

app = FastAPI()
# uvicorn backend.main:app --reload
# uvicorn backend.main:app --log-level debug


@app.get("/")
def home():
    return {"message": "LLM Engineering Project Started"}


@app.get("/ask")
def ask(question: str):

    result = execute(question)

    return {"question": question, "result": result}
