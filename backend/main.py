from fastapi import FastAPI
import tools

from backend.router import execute
from backend.logger import log_interaction

app = FastAPI()
# uvicorn backend.main:app --reload
# uvicorn backend.main:app --log-level debug


@app.get("/")
def home():
    return {"message": "LLM System Running"}


@app.get("/ask")
def ask(question: str):

    result = execute(question)
    # Feedback Logger
    log_interaction(question, result.get("answer"), result.get("plan"))

    return {"question": question, "result": result}
