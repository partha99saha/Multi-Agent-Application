# CortexAI Architecture

## Overview

CortexAI is an Enterprise Knowledge & Agent Platform designed for Retrieval-Augmented Generation (RAG), Multi-Agent Orchestration, Hybrid Search, Multimodal AI, and Evaluation Pipelines.

The platform combines:

* FastAPI backend services
* LangGraph agent orchestration
* Hybrid retrieval (BM25 + Vector Search)
* Fine-tuned embedding models
* OpenAI LLMs
* Qdrant Vector Database
* LangSmith Observability
* Multimodal Image & Audio Generation
* React-based Chat Interface

---

# High-Level Architecture

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    React UI     │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    FastAPI      │
                    │  API Gateway    │
                    └────────┬────────┘
                             │
               ┌─────────────┴─────────────┐
               │                           │
               ▼                           ▼
      ┌─────────────────┐       ┌─────────────────┐
      │ Session Manager │       │ Security Layer  │
      └────────┬────────┘       └────────┬────────┘
               │                         │
               └─────────────┬───────────┘
                             ▼
                    ┌─────────────────┐
                    │   LangGraph     │
                    │ Agent Workflow  │
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   Planner Agent      RAG Agent          Tool Agents
         │                   │                   │
         ▼                   ▼                   ▼
  Retriever Agent    Context Agent     Image / Audio
         │                   │
         ▼                   ▼
    BM25 + Qdrant      Context Builder
         │
         ▼
   Reranker Agent
         │
         ▼
   Answer Agent
         │
         ▼
    Critic Agent
         │
         ▼
      OpenAI
         │
         ▼
      Response
```

---

# End-to-End RAG Flow

```text
User Question
      │
      ▼
FastAPI API
      │
      ▼
Security Validation
      │
      ▼
Retriever
      │
      ├── BM25 Search
      │
      └── Qdrant Vector Search
      │
      ▼
Hybrid Results
      │
      ▼
Reranker
      │
      ▼
Top Context Chunks
      │
      ▼
Context Builder
      │
      ▼
Prompt Construction
      │
      ▼
OpenAI LLM
      │
      ▼
Critic Validation
      │
      ▼
Final Response
```

---

# Knowledge Ingestion Flow

```text
PDF / DOCX / TXT
        │
        ▼
Document Loader
        │
        ▼
Chunking
        │
        ▼
Embedding Generation
        │
        ▼
Qdrant Storage
        │
        ▼
BM25 Index Creation
        │
        ▼
Hybrid Search Ready
```

---

# Agent Architecture

CortexAI contains a dedicated agent framework powered by LangGraph.

Current Agents:

| Agent           | Responsibility                 |
| --------------- | ------------------------------ |
| Planner Agent   | Determines execution strategy  |
| Retriever Agent | Retrieves relevant documents   |
| Reranker Agent  | Improves retrieval quality     |
| Context Agent   | Builds optimized context       |
| Answer Agent    | Generates final answer         |
| Critic Agent    | Evaluates answer quality       |
| RAG Agent       | Coordinates retrieval workflow |
| Image Agent     | Handles image generation       |
| Audio Agent     | Handles text-to-speech         |

Current status:

* Agent infrastructure is implemented.
* Main production APIs currently use `backend/rag.py`.
* LangGraph orchestration is available for future expansion.

---

# Retrieval Architecture

## Hybrid Search

Frameworks Used:

* Qdrant
* Rank-BM25
* LangChain-Qdrant

Process:

```text
Question
   │
   ▼
BM25 Search
   │
   ├── Keyword Matching
   │
Vector Search
   │
   └── Semantic Matching
   │
   ▼
Merged Results
   │
   ▼
Reranker
   │
   ▼
Top Context
```

Benefits:

* Better recall
* Better precision
* Handles exact keywords
* Handles semantic similarity

---

# Embedding Architecture

Frameworks Used:

* SentenceTransformers
* PyTorch
* HuggingFace Transformers

Process:

```text
Document
    │
    ▼
Chunking
    │
    ▼
Embedding Model
    │
    ▼
Vector Representation
    │
    ▼
Qdrant Storage
```

Fine-Tuning Pipeline:

```text
Raw Documents
      │
      ▼
Dataset Builder
      │
      ▼
Triplet Builder
      │
      ▼
Triplet Training
      │
      ▼
Fine-Tuned Embedding Model
```

---

# LangGraph Architecture

Framework Used:

* LangGraph

Purpose:

* Agent orchestration
* State management
* Workflow routing
* Multi-step execution

Graph Components:

```text
State
  │
  ▼
Planner
  │
  ▼
Retriever
  │
  ▼
Reranker
  │
  ▼
Context Builder
  │
  ▼
Answer
  │
  ▼
Critic
```

---

# Session Management

Purpose:

* Manage chat sessions
* Track active requests
* Support cancellation
* Maintain conversation state

Features:

* Session creation
* Session switching
* Session deletion
* Active task tracking
* Task cancellation

Storage:

```text
Browser Local Storage
+
Backend Session Registry
```

---

# Security Layer

Purpose:

Protect the system from malicious prompts and misuse.

Features:

* Prompt injection detection
* Request validation
* Safety filtering
* Rate limiting

Frameworks:

* SlowAPI
* Custom security middleware

---

# Multimodal Architecture

## Image Generation

Frameworks:

* Diffusers
* HuggingFace Models
* PyTorch

Flow:

```text
Prompt
   │
   ▼
Image Tool
   │
   ▼
Diffusion Model
   │
   ▼
Generated Image
```

---

## Audio Generation

Frameworks:

* gTTS
* PyTorch Audio

Flow:

```text
Text
 │
 ▼
TTS Tool
 │
 ▼
Audio File
 │
 ▼
Playback
```

---

# Evaluation Architecture

Frameworks:

* RAGAS
* Evaluate
* Datasets

Metrics:

* Faithfulness
* Relevancy
* Context Precision
* Context Recall

Process:

```text
Dataset
   │
   ▼
RAG Pipeline
   │
   ▼
Evaluation
   │
   ▼
Metrics Report
```

---

# LangSmith Observability

Framework:

* LangSmith

Purpose:

* Trace requests
* Monitor prompts
* Track LLM calls
* Debug workflows
* Analyze performance

Flow:

```text
User Request
     │
     ▼
LangChain / LangGraph
     │
     ▼
LangSmith Trace
     │
     ▼
Monitoring Dashboard
```

---

# Infrastructure Components

| Component        | Technology               |
| ---------------- | ------------------------ |
| Frontend         | React + Vite             |
| Backend          | FastAPI                  |
| LLM              | OpenAI GPT-4o-mini       |
| Agent Framework  | LangGraph                |
| RAG Framework    | LangChain                |
| Vector Database  | Qdrant                   |
| Embeddings       | SentenceTransformers     |
| Reranking        | Cross Encoder            |
| Evaluation       | RAGAS                    |
| Monitoring       | LangSmith                |
| Image Generation | Diffusers                |
| Audio Generation | gTTS                     |
| Storage          | Local Filesystem         |
| Session Storage  | Browser + Backend Memory |

---

# API Reference

Base URL:

```text
http://localhost:8000
```

---

# Health Check

## GET /health

Checks API and Vector Database status.

### Response

```json
{
  "status": "healthy",
  "qdrant": "up"
}
```

---

# Session APIs

## POST /session/create

Creates a new session.

### Response

```json
{
  "session_id": "c4c2c3e9-4c4f-4e75-b18a-45f7cb66f7f"
}
```

---

## GET /session/{session_id}

Returns session information.

### Example

```http
GET /session/c4c2c3e9-4c4f-4e75-b18a-45f7cb66f7f
```

### Response

```json
{
  "history": [],
  "created_at": 1712345678.12,
  "active_task": null,
  "cancel_tasks": []
}
```

---

# Cancellation API

## POST /cancel/{session_id}/{task_id}

Cancels a running task.

### Response

```json
{
  "status": "cancel_requested"
}
```

---

# LLM API

## GET /ask

Direct LLM query without RAG.

### Parameters

| Parameter  | Type   | Required |
| ---------- | ------ | -------- |
| question   | string | Yes      |
| session_id | string | No       |

### Example

```http
GET /ask?question=What is AWS S3?
```

### Response

```json
{
  "task_id": "abc9b8ab-de2e-40ac-9b15-47abe54c4f5e",
  "question": "What is AWS S3?",
  "answer": "Amazon S3 is an object storage service..."
}
```

---

# RAG API

## GET /rag

Performs Hybrid Retrieval + Reranking + LLM Generation.

### Parameters

| Parameter  | Type   | Required |
| ---------- | ------ | -------- |
| question   | string | Yes      |
| session_id | string | Yes      |

### Example

```http
GET /rag?question=What is Azure Function App?&session_id=123
```

### Response

```json
{
  "task_id": "7c73f57e-3b56-4b12-b4d0-f0ef27b4f947",
  "question": "What is Azure Function App?",
  "answer": "Azure Function App is a serverless compute service..."
}
```

---

# Image Generation API

## GET /image

Generates images using the registered Image Tool.

### Parameters

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| prompt    | string | Yes      |

### Example

```http
GET /image?prompt=Cloud Architecture Diagram
```

### Response

```json
{
  "type": "image",
  "path": "data/img_-2564836775763627831.png"
}
```

---

# Audio Generation API

## GET /audio

Converts text into speech using TTS Tool.

### Parameters

| Parameter | Type   | Required |
| --------- | ------ | -------- |
| text      | string | Yes      |

### Example

```http
GET /audio?text=Hello CortexAI
```

### Response

```json
{
  "type": "audio",
  "path": "data/audio_123456.mp3"
}
```

---

# File Upload API

## POST /upload

Uploads documents for ingestion and vectorization.

### Supported Formats

* PDF
* TXT
* DOCX
* Markdown

### Request

```http
POST /upload
Content-Type: multipart/form-data
```

### Form Data

```text
file=<document>
```

### Response

```json
{
  "status": "success",
  "chunks": 125,
  "vectors_created": 125
}
```

---

# Typical RAG Request Flow

```text
User Question
      │
      ▼
GET /rag
      │
      ▼
Prompt Injection Check
      │
      ▼
BM25 Retrieval
      │
      ▼
Qdrant Retrieval
      │
      ▼
Hybrid Merge
      │
      ▼
Cross-Encoder Reranking
      │
      ▼
Context Builder
      │
      ▼
GPT-4o-mini
      │
      ▼
Answer
```

---

# Typical Upload Flow

```text
Upload File
     │
     ▼
Loader
     │
     ▼
Chunker
     │
     ▼
Embedding Model
     │
     ▼
Qdrant
     │
     ▼
BM25 Index
```

---

# Rate Limits

```text
/ask  -> 10 requests/minute
/rag  -> 10 requests/minute
```

Implemented using:

```text
slowapi
```

---

# Error Response Format

```json
{
  "error": "message"
}
```

### Examples

```json
{
  "error": "Too many requests"
}
```

```json
{
  "answer": "I cannot assist with that request."
}
```

```json
{
  "answer": "An error occurred while processing your request."
}
```

---

# Summary

CortexAI is a production-ready AI platform that combines:

* Enterprise RAG
* Hybrid Search
* LangGraph Agent Infrastructure
* Fine-Tuned Embeddings
* Multimodal Capabilities
* Evaluation Pipelines
* LangSmith Observability
* Secure FastAPI Services

The architecture is designed to evolve from a traditional RAG system into a fully orchestrated multi-agent enterprise AI platform.
