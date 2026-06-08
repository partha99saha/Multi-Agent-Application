import os
import uuid
import shutil
from fastapi import APIRouter, UploadFile, File, HTTPException
from ingestion.ingest import ingest_file

router = APIRouter()

# -------------------------
# CONFIG
# -------------------------
UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = {".pdf", ".docx", ".xlsx", ".txt"}
MAX_FILE_SIZE_MB = 50


# -------------------------
# VALIDATION
# -------------------------
def validate_file(file: UploadFile):

    # 1. Extension check
    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")

    # 2. Size check
    file.file.seek(0, os.SEEK_END)
    size = file.file.tell()
    file.file.seek(0)

    if size > MAX_FILE_SIZE_MB * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail=f"File too large. Max allowed is {MAX_FILE_SIZE_MB}MB",
        )


# -------------------------
# SAVE FILE SAFELY
# -------------------------
def save_file(file: UploadFile):

    safe_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, safe_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path


# -------------------------
# API ENDPOINT
# -------------------------
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    validate_file(file)

    file_path = save_file(file)

    result = ingest_file(file_path)

    return {
        "message": "File uploaded and indexed successfully",
        "file_path": file_path,
        "chunks_indexed": result["chunks_indexed"],
    }
