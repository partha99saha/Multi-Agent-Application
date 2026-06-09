# LLM Engineering - Flow Design & System Design Interview Notes

# 1. End-to-End LLM Application Flow

```text
User
 ↓
Frontend / API Gateway
 ↓
Authentication
 ↓
Rate Limiter
 ↓
Prompt Validation
 ↓
LLM Application Layer
 ↓
Prompt Builder
 ↓
Model Provider
 ↓
LLM
 ↓
Response Parser
 ↓
Safety Filter
 ↓
Response
```

### Interview Question

**Q. Explain the flow of a basic LLM application.**

**Answer:**

A user sends a request through a frontend or API. The request is authenticated, validated, and converted into a prompt. The prompt is sent to the LLM provider. The generated response is parsed, validated, optionally filtered by safety rules, and returned to the user.

---

# 2. Enterprise RAG Flow

```text
User
 ↓
Frontend
 ↓
API Gateway
 ↓
Authentication
 ↓
Rate Limiter
 ↓
LangGraph
 ↓
Planner
 ↓
Retriever
 ↓
BM25 Search
 ↓
Vector Search
 ↓
Hybrid Retrieval
 ↓
Reranker
 ↓
Context Builder
 ↓
LLM
 ↓
Critic
 ↓
Response
```

Supporting Components

```text
Session Management
Prompt Cache
Evaluation Layer
LangSmith
Fine-Tuned Embeddings
Tool Calling
Image Generation
Audio Generation
Upload Pipeline
Security Layer
```

### Libraries

* LangSmith
* OpenTelemetry
* MLflow


### Interview Question

**Q. Explain a production RAG pipeline.**

**Answer:**

The user query is first rewritten and optimized. Hybrid retrieval combines keyword search (BM25) and semantic search (vector search). Retrieved documents are reranked and compressed into a context window. The context is injected into a prompt and sent to the LLM. A critic or evaluator can validate the answer before returning it.

---

# 3. Hybrid Search Flow

```text
Question
      ↓
 ┌──────────────┐
 │ Hybrid Layer │
 └──────────────┘
      ↓
BM25        Embeddings
 ↓               ↓
Keyword      Vector Search
Search
 ↓               ↓
 └──── Merge Results ────┘
             ↓
         Reranker
             ↓
       Top Documents
```

### Interview Question

**Q. Why combine BM25 and vector search?**

**Answer:**

BM25 excels at exact keyword matching, while vector search excels at semantic similarity. Hybrid retrieval improves recall and reduces retrieval failures.

---

# 4. Agentic RAG Flow

```text
User
 ↓
Planner Agent
 ↓
Retriever Agent
 ↓
Reranker Agent
 ↓
Context Agent
 ↓
Answer Agent
 ↓
Critic Agent
 ↓
Response
```

### Interview Question

**Q. What is Agentic RAG?**

**Answer:**

Agentic RAG decomposes the RAG workflow into specialized agents. Each agent performs a dedicated task, improving modularity, reasoning quality, and maintainability.

---

# 5. Multi-Agent System Design

```text
User
 ↓
Supervisor Agent
 ├───────────────┐
 ↓               ↓
Research     Tool Agent
Agent
 ↓               ↓
Data        External APIs
 ↓               ↓
 └───── Aggregator Agent ────┘
                 ↓
             Critic Agent
                 ↓
             Final Answer
```

### Interview Question

**Q. Why use multiple agents instead of one?**

**Answer:**

Multiple agents provide separation of concerns. Each agent specializes in a task such as planning, retrieval, tool execution, or validation. This improves scalability and debugging.

---

# 6. LangGraph Architecture

```text
START
 ↓
Planner
 ↓
Retriever
 ↓
Reranker
 ↓
Answer
 ↓
Critic
 ↓
END
```

Conditional Flow:

```text
Critic
 ↓
Confidence < Threshold
 ↓
Retrieve More Context
 ↓
Answer Again
```

### Interview Question

**Q. Why use LangGraph instead of LangChain?**

**Answer:**

LangGraph supports stateful workflows, loops, retries, conditional routing, multi-agent systems, and human-in-the-loop interactions.

---

# 7. MCP Architecture

```text
LLM
 ↓
MCP Client
 ↓
MCP Protocol
 ↓
MCP Server
 ↓
Tools
 ↓
External Systems
```

Examples:

```text
Database
Slack
GitHub
Jira
Confluence
Filesystem
```

### Interview Question

**Q. What problem does MCP solve?**

**Answer:**

MCP standardizes communication between AI applications and external tools, eliminating custom integrations for every tool.

---

# 8. Tool Calling Architecture

```text
User Question
 ↓
LLM
 ↓
Tool Selection
 ↓
Tool Execution
 ↓
Tool Response
 ↓
LLM
 ↓
Final Response
```

### Interview Question

**Q. How does tool calling work?**

**Answer:**

The LLM decides whether a tool is needed. The selected tool executes, returns structured output, and the LLM uses that output to generate the final response.

---

# 9. Fine-Tuning Architecture

```text
Raw Data
 ↓
Cleaning
 ↓
Instruction Dataset
 ↓
Tokenization
 ↓
LoRA / QLoRA Training
 ↓
Checkpoint
 ↓
Fine-Tuned Model
```

### Interview Question

**Q. When should you fine-tune instead of using RAG?**

**Answer:**

Fine-tuning is used when changing model behavior, style, formatting, or reasoning. RAG is used when adding new knowledge.

---

# 10. Embedding Training Flow

```text
Documents
 ↓
Triplet Generation
 ↓
Anchor
Positive
Negative
 ↓
Sentence Transformer
 ↓
Contrastive Loss
 ↓
Fine-Tuned Embeddings
```

### Interview Question

**Q. Why train custom embeddings?**

**Answer:**

Domain-specific embeddings improve retrieval accuracy by learning semantic relationships unique to enterprise data.

---

# 11. Evaluation Pipeline

```text
Question
 ↓
Retriever
 ↓
Documents
 ↓
LLM
 ↓
Answer
 ↓
Evaluator
 ↓
Metrics
```

Metrics:

```text
Faithfulness
Answer Relevancy
Context Precision
Context Recall
Latency
Cost
```

---

# 12. LLMOps Architecture

```text
Prompt Management
       ↓
Version Control
       ↓
Evaluation
       ↓
Monitoring
       ↓
Tracing
       ↓
Deployment
       ↓
Production
```

### Tools

* LangSmith
* Ragas
* DeepEval
* OpenAI Evals
* MLflow

### Responsibilities

* Evaluation
* Monitoring
* Versioning
* Deployment
* Observability


### Interview Question

**Q. What is LLMOps?**

**Answer:**

LLMOps applies DevOps practices to LLM systems, including deployment, monitoring, evaluation, observability, and governance.

---

# 13. LangSmith Observability Flow

```text
User Request
 ↓
LangGraph
 ↓
Retriever
 ↓
Tool Calls
 ↓
LLM Calls
 ↓
LangSmith Tracing
 ↓
Dashboard
```

Tracks:

```text
Prompt
Context
Tokens
Latency
Cost
Errors
Tool Calls
Agent Steps
```

---

# 14. Enterprise AI Platform Architecture

```text
User
 ↓
Frontend
 ↓
API Gateway
 ↓
Authentication
 ↓
Rate Limiter
 ↓
LangGraph
 ↓
Planner
 ↓
Retriever
 ↓
BM25 + Qdrant
 ↓
Reranker
 ↓
Context Builder
 ↓
LLM
 ↓
Critic
 ↓
Response
```

Supporting Services:

```text
Session Management
Prompt Cache
Evaluation Layer
LangSmith
Fine-Tuned Embeddings
Tool Calling
Image Generation
Audio Generation
Upload Pipeline
Security Layer
```

---

# 15. Most Common System Design Questions

### Q. Design a Production RAG System

Focus:

* Hybrid Retrieval
* Reranking
* Context Building
* Hallucination Reduction
* Evaluation

---

### Q. Design an Agentic AI System

Focus:

* Planner
* Tool Calling
* Memory
* Multi-Agent Coordination
* LangGraph

---

### Q. Design a ChatGPT-like Application

Focus:

* Conversation Memory
* Session Management
* Streaming Responses
* Prompt Caching
* Monitoring

---

### Q. Design an Enterprise Knowledge Assistant

Focus:

* Document Ingestion
* Embeddings
* Hybrid Search
* Access Control
* Audit Logs

---

### Q. Design a Scalable AI Platform

Focus:

* API Gateway
* Load Balancing
* Vector Database
* LLM Provider
* Monitoring
* Evaluation
* Security
* Observability

```
```
