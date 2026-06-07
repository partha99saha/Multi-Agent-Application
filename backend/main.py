from fastapi import FastAPI
import tools

from backend.router import execute
from backend.logger import log_interaction
from backend.feedback import save_feedback

app = FastAPI()
# uvicorn backend.main:app --reload
# uvicorn backend.main:app --log-level debug


@app.get("/")
def home():
    return {"message": "LLM System Running"}


@app.get("/ask")
def ask(question: str):

    result = execute(question)

    log_interaction(question, result.get("answer"), result.get("plan"))

    return {"question": question, "result": result}


@app.get("/feedback")
def feedback(question: str, rating: int):

    # rating = +1 or -1
    save_feedback(question, "unknown", rating)

    return {"status": "feedback saved"}
