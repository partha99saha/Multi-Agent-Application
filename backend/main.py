from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from backend.logger import logger
import uuid

# ---------------------------
# CORE IMPORTS
# ---------------------------
from backend.llm import ask_llm
from backend.rag import ask_rag
from backend.upload import router as upload_router
from tools.tool_registry import get_tool

from backend.session_manager import (
    create_session,
    get_session,
    cancel_task,
    set_active_task,
)

# ---------------------------
# APP INIT
# ---------------------------
app = FastAPI(title="Multi-Agent LLM System")
app.include_router(upload_router)
app.mount(
    "/data",
    StaticFiles(directory="data"),
    name="data",
)

# ---------------------------
# CORS
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# uvicorn backend.main:app --reload
# ---------------------------
# RATE LIMITING
# ---------------------------
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(status_code=429, content={"error": "Too many requests"})


# ---------------------------
# STARTUP WARMUP
# ---------------------------
@app.on_event("startup")
def warmup():
    logger.info("Warming up system...")
    from backend.session_manager import cleanup_sessions

    cleanup_sessions()

    try:
        ask_llm("warmup", session_id="warmup", task_id="warmup")
    except:
        pass

    try:
        from vectorstore.embedding import get_model

        get_model()
    except:
        pass

    logger.info("System Ready")


# ---------------------------
# BASIC ROUTE
# ---------------------------
@app.get("/health")
def health():

    try:
        from vectorstore.client import client

        client.get_collections()

        qdrant_status = "up"

    except Exception:
        qdrant_status = "down"

    return {
        "status": "healthy",
        "qdrant": qdrant_status,
    }


# ---------------------------
# SESSION APIs
# ---------------------------
@app.post("/session/create")
def new_session():
    return {"session_id": create_session()}


@app.get("/session/{session_id}")
def session_info(session_id: str):
    return get_session(session_id)


@app.post("/cancel/{session_id}/{task_id}")
def cancel(session_id: str, task_id: str):
    cancel_task(session_id, task_id)
    return {"status": "cancel_requested"}


# ---------------------------
# LLM (NO RAG)
# ---------------------------
@app.get("/ask")
@limiter.limit("10/minute")
def ask(request: Request, question: str, session_id: str = None):

    task_id = str(uuid.uuid4())

    answer = ask_llm(question, session_id=session_id, task_id=task_id)

    return {"task_id": task_id, "question": question, "answer": answer}


# ---------------------------
# RAG PIPELINE
# ---------------------------
@app.get("/rag")
@limiter.limit("10/minute")
def rag(request: Request, question: str, session_id: str):

    task_id = str(uuid.uuid4())

    set_active_task(session_id, task_id)

    result = ask_rag(question, session_id=session_id, task_id=task_id)

    return {"task_id": task_id, "question": question, "answer": result["answer"]}


# ---------------------------
# MULTIMODAL TOOLS
# ---------------------------
@app.get("/image")
def image(prompt: str, session_id: str = None):

    tool = get_tool("image")
    response = tool(prompt)
    return response


@app.get("/audio")
def audio(text: str, session_id: str = None):

    tool = get_tool("tts")
    response = tool(text)
    return response
