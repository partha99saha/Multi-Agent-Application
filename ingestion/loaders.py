from pypdf import PdfReader
import pandas as pd
from docx import Document


def load_pdf(file_path: str):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text


def load_docx(file_path: str):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])


def load_excel(file_path: str):
    df = pd.read_excel(file_path)
    return df.astype(str).to_string()


def load_txt(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def load_document(file_path: str):
    if file_path.endswith(".pdf"):
        return load_pdf(file_path)

    if file_path.endswith(".docx"):
        return load_docx(file_path)

    if file_path.endswith(".xlsx"):
        return load_excel(file_path)

    if file_path.endswith(".txt"):
        return load_txt(file_path)

    raise ValueError("Unsupported file type")
