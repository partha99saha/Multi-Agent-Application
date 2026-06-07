from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# import tools
# from backend.router import execute
# from backend.logger import log_interaction
# from backend.feedback import save_feedback
from backend.llm import ask_llm
from backend.rag import ask_rag

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

from tools.tool_registry import get_tool

app = FastAPI(title="Multi-Agent LLM System")

# ---------------------------
# CORS (IMPORTANT)
# ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# RATE LIMITING (DDoS SAFETY)
# ---------------------------
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(status_code=429, content={"error": "Too many requests"})


# ---------------------------
# WARMUP (IMPORTANT)
# ---------------------------
@app.on_event("startup")
def warmup():
    """
    Load models once at startup to avoid cold-start latency.
    """
    print("Warming up LLM + Embeddings...")

    try:
        ask_llm("warmup")
    except:
        pass

    try:
        from vectorstore.embedding import get_model

        get_model()
    except:
        pass

    print("System Ready")


# ---------------------------
# ROUTES
# ---------------------------
@app.get("/")
def home():
    return {"message": "LLM System Running"}


@app.get("/ask")
@limiter.limit("10/minute")
def ask(request: Request, question: str):

    answer = ask_llm(question)

    return {"question": question, "answer": answer}


@app.get("/rag")
@limiter.limit("10/minute")
def rag(request: Request, question: str):

    result = ask_rag(question)

    return result


# ---------------------------
# MULTIMODAL ROUTES
# ---------------------------
@app.get("/image")
def image(prompt: str):

    tool = get_tool("image")
    return tool(prompt)


@app.get("/audio")
def audio(text: str):

    tool = get_tool("tts")
    return tool(text)
