# CortexAI
CortexAI — Enterprise Knowledge & Agent Platform

Enterprise Knowledge & Agent Platform built using FastAPI, LangGraph, Hybrid RAG, Fine-Tuned Embeddings, Multimodal Tools, LangSmith Observability, and Multi-Agent Orchestration.

---

# Overview

CortexAI is a production-ready AI platform designed for enterprise knowledge retrieval and intelligent task execution.

The platform combines:

* Multi-Agent Orchestration
* Retrieval-Augmented Generation (RAG)
* Hybrid Search (Vector + BM25)
* Fine-Tuned Embeddings
* LangGraph Workflows
* LangSmith Monitoring
* Image Generation
* Audio Generation
* Session Management
* Evaluation Pipelines
* Security Controls


# Infrastructure Requirements

## Operating System

* Windows 10/11
* Linux
* macOS

## Python

```text
Python 3.11.3
```

## Node.js

```text
Node.js 20+
```

## Vector Database

```text
Qdrant
```

Docker Example:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

## GPU (Optional)

Recommended:

```text
NVIDIA GPU
CUDA 12.1
```

Used for:

* Embedding Training
* Reranking
* Diffusion Models
* Transformers

---

# Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=
HF_TOKEN=
LANGSMITH_API_KEY=
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_PROJECT=CortexAI
LLM_MODEL=gpt-4o-mini
```

---

# Installation

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install PyTorch

CUDA 12.1

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

---

# Install Additional Binary Package

```bash
pip install scikit-network --only-binary=:all:
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running Qdrant

Docker:

```bash
docker run -p 6333:6333 qdrant/qdrant
```

Verify:

```text
http://localhost:6333/dashboard
```

---

# Running Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger:

```text
http://localhost:8000/docs
```

---

# Running Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

---

# Project Structure

```text
CortexAI
│
├── agents/
├── backend/
├── core/
├── data/
├── evaluation/
├── fine_tuning/
├── fine_tuned_embedding_model/
├── frontend/
├── ingestion/
├── langchain_rag/
├── llm/
├── tools/
├── utils/
├── vectorstore/
│
├── requirements.txt
├── README.md
└── Architecture.md
```

---

# Folder Descriptions

## agents/

LangGraph-based agent orchestration layer.

### Files

* planner.py → Task planning agent
* retriever_agent.py → Retrieval agent
* reranker_agent.py → Reranking agent
* context_agent.py → Context construction
* answer_agent.py → Response generation
* critic_agent.py → Response validation
* image_agent.py → Image workflow
* audio_agent.py → Audio workflow
* rag_agent.py → End-to-end RAG agent
* graph.py → LangGraph definition
* state.py → Shared workflow state
* router.py → Agent routing logic

---

## backend/

Core application services.

### Files

* main.py → FastAPI entry point
* llm.py → OpenAI integration
* rag.py → RAG pipeline
* upload.py → File upload API
* session_manager.py → Session lifecycle
* security.py → Prompt injection detection
* safety.py → Safety layer
* router.py → Request routing
* planner.py → Backend planner
* feedback.py → User feedback APIs
* logger.py → Logging configuration
* token_optimizer.py → Token reduction logic
* model_selector.py → Model selection
* mcp.py → MCP integration

---

## core/

Shared core schemas and MCP utilities.

### Files

* schemas.py
* mcp.py

---

## data/

Knowledge documents used for ingestion.

Examples:

* aws.pdf
* azure.pdf
* system_design.pdf

---

## evaluation/

RAG evaluation framework.

### Files

* rag_evaluator.py
* evaluate_rag.py
* confidence.py
* dataset.json

---

## fine_tuning/

Embedding training pipeline.

### Files

* build_dataset.py
* build_triplets.py
* train_embeddings.py

---

## fine_tuned_embedding_model/

Trained Sentence Transformer embedding model.

Contains:

* tokenizer
* pooling layer
* configs
* weights

---

## ingestion/

Document ingestion pipeline.

### Files

* loaders.py
* pdf_loader.py
* ingest.py
* ingest_folder.py
* ingest_pdf.py
* chunker.py

---

## langchain_rag/

Alternative LangChain implementation.

### Files

* chain.py
* retriever.py
* vectorstore.py
* splitter.py
* loaders.py

---

## llm/

LLM helper utilities.

### Files

* query_rewriter.py

---

## tools/

Tool calling layer.

### Files

* llm_tool.py
* rag_tool.py
* image_tool.py
* audio_tool.py
* tool_registry.py

---

## utils/

Reusable utility components.

### Files

* config.py
* timer.py
* prompt_cache.py
* token_optimizer.py

---

## vectorstore/

Hybrid retrieval infrastructure.

### Files

* embedding.py
* retriever.py
* hybrid_retriever.py
* reranker.py
* similarity.py
* bm25_store.py
* build_bm25_index.py
* qdrant_store.py

---

# Major Features

## Multi-Agent Orchestration

Implemented using LangGraph.

Agents collaborate through shared state.

---

## Hybrid Retrieval

Combines:

* Qdrant Vector Search
* BM25 Lexical Search

Improves retrieval quality.

---

## Fine-Tuned Embeddings

Custom embedding model trained using:

* Triplet Loss
* Sentence Transformers

Improves enterprise document retrieval.

---

## LangSmith Observability

Provides:

* Tracing
* Debugging
* Performance Monitoring
* Prompt Inspection

---

## Security Layer

Includes:

* Prompt Injection Detection
* Request Validation
* Safety Filters

---

## Session Management

Features:

* Session Creation
* Session Tracking
* Task Cancellation
* Browser Persistence

---

## Multimodal Support

### Image Generation

```text
/image
```

### Audio Generation

```text
/tts
```

---

## Evaluation Framework

Measures:

* Faithfulness
* Context Precision
* Answer Relevancy
* Confidence

Using:

* RAGAS
* LangSmith
* Custom Evaluators

---
# Complete Libraries & Packages

| Library                  | Purpose                               |
| ------------------------ | ------------------------------------- |
| fastapi                  | REST API framework                    |
| uvicorn                  | ASGI server for FastAPI               |
| slowapi                  | Rate limiting and API protection      |
| openai                   | OpenAI model integration              |
| langchain                | Core LangChain framework              |
| langchain-community      | Community integrations                |
| langchain-openai         | OpenAI integration for LangChain      |
| langchain-text-splitters | Document chunking utilities           |
| langchain-qdrant         | Qdrant integration                    |
| langgraph                | Multi-agent workflow orchestration    |
| llama-index              | Alternative RAG framework             |
| qdrant-client            | Qdrant vector database client         |
| sentence-transformers    | Embedding generation                  |
| torch                    | Deep learning framework               |
| torchvision              | Computer vision utilities             |
| torchaudio               | Audio processing                      |
| accelerate               | Faster model inference                |
| transformers             | HuggingFace transformer models        |
| diffusers                | Image generation models               |
| safetensors              | Secure model weight loading           |
| rank-bm25                | BM25 lexical retrieval                |
| pypdf                    | PDF document parsing                  |
| python-docx              | Microsoft Word document parsing       |
| pandas                   | Data processing and analytics         |
| openpyxl                 | Excel file processing                 |
| gtts                     | Google Text-to-Speech                 |
| click                    | CLI utilities                         |
| pytesseract              | OCR text extraction                   |
| pillow                   | Image processing                      |
| ragas                    | RAG evaluation framework              |
| datasets                 | Dataset management                    |
| evaluate                 | Evaluation metrics                    |
| langsmith                | Tracing, monitoring and observability |
| scikit-learn             | Machine learning utilities            |
| pytest-asyncio           | Async testing                         |
| python-dotenv            | Environment variable loading          |
| pydantic                 | Data validation and schemas           |
| sqlalchemy               | ORM and database abstraction          |
| python-multipart         | File upload support                   |
| scikit-network           | Graph/network algorithms              |

---

# Core AI Stack

```text
OpenAI
LangChain
LangGraph
SentenceTransformers
Transformers
Torch
Diffusers
```

Used for:

* LLM Inference
* Agent Workflows
* Embeddings
* Image Generation
* Audio Processing

---

# Retrieval Stack

```text
Qdrant
BM25
LangChain-Qdrant
Rank-BM25
```

Used for:

* Hybrid Search
* Vector Search
* Semantic Retrieval
* Keyword Retrieval

---

# Evaluation Stack

```text
RAGAS
Evaluate
Datasets
LangSmith
```

Used for:

* Faithfulness
* Relevancy
* Context Precision
* Experiment Tracking

---

# Document Processing Stack

```text
PyPDF
Python-Docx
OpenPyXL
Pillow
PyTesseract
```

Used for:

* PDF Processing
* DOCX Processing
* Excel Processing
* OCR
* Image Extraction

---

# Backend Stack

```text
FastAPI
Uvicorn
SlowAPI
Pydantic
SQLAlchemy
Python-Multipart
```

Used for:

* REST APIs
* Validation
* Uploads
* Rate Limiting
* Persistence

---

# Utility Stack

```text
Pandas
Click
Python-Dotenv
SafeTensors
Accelerate
```

Used for:

* Data Engineering
* Configuration
* Performance Optimization
* Model Loading

---

# Future Enhancements

* Autonomous Agent Loops
* Dynamic Tool Selection
* Web Search Agent
* SQL Agent
* Memory Agent
* Research Agent
* Report Generation Agent
* Multi-Modal Planning Agent
* Human-in-the-Loop Approval Workflows

