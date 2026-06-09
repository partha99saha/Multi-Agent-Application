# LLM Engineering Interview Questions & Answers (Part 2)

## 16. Hugging Face

### Q. What is Hugging Face?

Hugging Face is the most widely used open-source ecosystem for building, training, fine-tuning, evaluating, and deploying NLP and LLM applications.

Core offerings:

* Transformers
* Datasets
* Tokenizers
* Accelerate
* PEFT
* TRL
* Hub
* Inference Endpoints

---

### Q. What is the Transformers Library?

A library that provides pre-trained models for:

* NLP
* Vision
* Audio
* Multimodal AI

Examples:

```python
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
```

---

### Q. What is the Hugging Face Hub?

A centralized model repository similar to GitHub for AI models.

Contains:

* LLMs
* Embedding Models
* Rerankers
* Datasets
* Spaces

Examples:

* Llama
* Mistral
* Phi
* BGE
* E5

---

### Q. What is Accelerate?

A framework for:

* Multi-GPU training
* Distributed training
* Mixed precision

without writing complex distributed code.

---

### Q. What is PEFT?

Parameter Efficient Fine-Tuning.

Instead of training the entire model:

```text
Train small adapter layers
```

Benefits:

* Less memory
* Faster training
* Lower cost

Libraries:

```python
peft
```

---

### Q. What is TRL?

Transformer Reinforcement Learning.

Used for:

* RLHF
* DPO
* PPO

Libraries:

```python
trl
```

---

## 17. LangChain

### Q. What is LangChain?

LangChain is an orchestration framework for building LLM applications.

Provides:

* Prompt Templates
* Chains
* Retrievers
* Agents
* Memory
* Tool Calling

---

### Q. What Problem Does LangChain Solve?

Without LangChain:

```text
Manual Prompt Handling
Manual Retrieval
Manual Tool Execution
```

LangChain standardizes these workflows.

---

### Q. What is LCEL?

LangChain Expression Language.

Example:

```python
prompt | llm | parser
```

Benefits:

* Composable
* Modular
* Easy debugging

---

### Q. What is a Chain?

A sequence of operations.

Example:

```text
Prompt
↓
LLM
↓
Parser
```

---

### Q. What are Retrievers in LangChain?

Components that fetch relevant documents.

Examples:

```text
Vector Retriever
BM25 Retriever
MultiQuery Retriever
Parent Document Retriever
```

---

### Q. What are LangChain Agents?

Agents decide:

```text
Which tool to use
When to use it
How to use it
```

instead of following fixed workflows.

---

### Q. LangChain vs LangGraph?

LangChain:

```text
Linear workflows
```

LangGraph:

```text
State-based agent workflows
```

LangGraph is generally preferred for production agent systems.

---

## 18. Memory Systems

### Memory System Architecture

```text
User
 ↓
Conversation
 ↓
Memory Manager
 ├──────────────┐
 ↓              ↓
Short-Term   Long-Term
Memory       Memory
 ↓              ↓
Context Builder
 ↓
Prompt
 ↓
LLM
```

### Memory Types

#### Short-Term Memory

Stores current conversation.

#### Long-Term Memory

Stores persistent user knowledge.

#### Semantic Memory

Stores facts and preferences.

#### Episodic Memory

Stores previous interactions.

### Q. Why Do LLM Applications Need Memory?

LLMs are stateless.

Without memory:

```text
Every request starts from zero.
```

---

### Q. Types of Memory?

1. Short-Term Memory
2. Long-Term Memory
3. Semantic Memory
4. Episodic Memory

---

### Q. What is Conversation Memory?

Stores previous messages.

Example:

```text
User: My name is John.
User: What's my name?
```

Memory enables correct answers.

---

### Q. What is Semantic Memory?

Stores facts.

Example:

```text
User prefers AWS.
```

---

### Q. What is Episodic Memory?

Stores experiences or past interactions.

Example:

```text
User previously solved Kubernetes issue.
```

---

## 19. Agent Engineering

### Q. What is an AI Agent?

An AI system capable of:

```text
Planning
Reasoning
Acting
Using Tools
```

to accomplish goals.

---

### Q. Agent vs LLM?

LLM:

```text
Generate Text
```

Agent:

```text
Think
Plan
Act
Observe
Repeat
```

---

### Q. What are Core Agent Components?

```text
Planner
Memory
Tools
Reasoner
Executor
```

---

### Q. What is ReAct?

Reason + Act.

Workflow:

```text
Thought
Action
Observation
Thought
Action
```

---

### Q. What Makes Agents Fail?

* Poor planning
* Tool failures
* Hallucinations
* Missing memory
* Weak prompts

---

## 20. Multi-Agent Systems

### Q. What is a Multi-Agent System?

Multiple specialized agents collaborate.

Example:

```text
Planner
Retriever
Reranker
Answer Agent
Critic
```

---

### Q. Why Use Multiple Agents?

Benefits:

* Separation of concerns
* Better scalability
* Better maintainability

---

### Q. What is Agent Delegation?

One agent assigns tasks to another agent.

Example:

```text
Planner
↓
Retriever
↓
Answer Agent
```

---

### Q. What is Agent Communication?

Agents exchange:

```text
Messages
State
Context
```

during execution.

---

## 21. LangGraph

### Q. What is LangGraph?

A graph-based orchestration framework for AI agents.

Built by LangChain.

---

### Q. Why Was LangGraph Created?

Traditional chains struggle with:

```text
Loops
State
Complex Agent Flows
```

LangGraph solves these limitations.

---

### Q. Core Concepts in LangGraph?

```text
State
Node
Edge
Graph
```

---

### Q. What is State?

Shared information passed between nodes.

Example:

```python
{
 "question": "...",
 "documents": [...]
}
```

---

### Q. What is a Node?

A node performs a task.

Examples:

```text
Planner
Retriever
Reranker
Critic
```

---
### 

### Q. What is a Conditional Edge?

Routing logic.

Example:

```text
If confidence < threshold
→ Retrieve More Context
```

---

### Q. Benefits of LangGraph?

* Durable execution
* Stateful workflows
* Multi-agent orchestration
* Human-in-the-loop

---

## 22. Fine-Tuning

### Q. What is Fine-Tuning?

Training a pre-trained model on domain-specific data.

---

### Q. Why Fine-Tune?

Improve:

* Style
* Domain Knowledge
* Formatting
* Specialized Tasks

---

### Q. Fine-Tuning vs RAG?

RAG:

```text
Adds Knowledge
```

Fine-Tuning:

```text
Changes Behavior
```

---

### Q. What is LoRA?

Low-Rank Adaptation.

Trains only small matrices instead of full weights.

Benefits:

* Faster
* Cheaper
* Less memory

---

### Q. What is QLoRA?

Quantized LoRA.

Combines:

```text
4-bit Quantization
+
LoRA
```

for efficient training.

---

### Q. Common Fine-Tuning Frameworks?

* PEFT
* TRL
* Transformers
* Axolotl
* Unsloth

---

## 23. Evaluation

### Q. Why Evaluate LLM Applications?

Because accuracy alone is insufficient.

Need to measure:

* Retrieval quality
* Faithfulness
* Grounding
* Hallucinations

---

### Q. What is Faithfulness?

Whether generated answers are supported by retrieved context.

---

### Q. What is Answer Relevance?

How well the answer addresses the question.

---

### Q. What is Context Recall?

Measures whether retrieval found necessary information.

---

### Q. What is Context Precision?

Measures whether retrieved content was relevant.

---

### Q. Popular Evaluation Frameworks?

* Ragas
* DeepEval
* LangSmith
* OpenAI Evals

---

## 24. Security

### Q. What is Prompt Injection?

Malicious instructions inserted into prompts.

Example:

```text
Ignore previous instructions.
```

---

### Q. What is Indirect Prompt Injection?

Malicious instructions hidden inside retrieved documents.

---

### Q. How Can Prompt Injection Be Mitigated?

* Input validation
* Safety filters
* Context isolation
* Output validation

---

### Q. What is PII Leakage?

Exposure of:

```text
Emails
Phone Numbers
Passwords
Personal Data
```

---

### Q. Security Layers in Enterprise LLMs?

* Authentication
* Authorization
* Prompt Filtering
* Rate Limiting
* Monitoring

### Security Architecture Flow

```text
User Input
      ↓
Authentication
      ↓
Authorization
      ↓
Rate Limiting
      ↓
Prompt Injection Detection
      ↓
Input Validation
      ↓
LLM / Tools
      ↓
Output Filtering
      ↓
Response
```

### Libraries

* FastAPI Security
* SlowAPI
* JWT
* OAuth2

### Risks

* Prompt Injection
* Data Leakage
* Jailbreak Attempts
* Unauthorized Access


---

## 25. Model Selection

### Q. How Do You Choose an LLM?

Consider:

* Accuracy
* Cost
* Latency
* Context Window
* Tool Calling

---

### Q. GPT vs Claude vs Gemini?

General comparison:

GPT:

* Strong ecosystem

Claude:

* Strong reasoning

Gemini:

* Strong multimodal capabilities

---

### Q. Open Source vs Closed Source?

Open Source:

* Customizable
* Self-hosted

Closed Source:

* Better managed
* Often higher performance

---

## 26. Inference Optimization

### Q. What is Quantization?

Reducing precision.

Example:

```text
FP32
→ FP16
→ INT8
→ INT4
```

Benefits:

* Faster inference
* Lower memory

---

### Q. What is KV Cache?

Stores previous attention computations.

Benefits:

* Faster token generation

---

### Q. What is Prompt Caching?

Reuse previously processed prompts.

Benefits:

* Lower latency
* Reduced costs

---

### Q. What is Batching?

Processing multiple requests together.

Benefits:

* Higher throughput

---

## 27. LLMOps

### Q. What is LLMOps?

Applying DevOps principles to LLM systems.

Includes:

* Deployment
* Monitoring
* Evaluation
* Observability

---

### Q. Components of LLMOps?

```text
Prompt Management
Evaluation
Monitoring
Versioning
Deployment
```

---

### Q. Why Is LLMOps Important?

LLM systems change frequently.

Need:

* Reliability
* Traceability
* Reproducibility

---

## 28. LangSmith

### Q. What is LangSmith?

An observability platform for LLM applications.

Provides:

* Tracing
* Debugging
* Evaluation
* Monitoring

---

### Q. What Problems Does LangSmith Solve?

Helps answer:

```text
Why did the model fail?
Which prompt caused it?
Which retrieval step was wrong?
```

---

### Q. What Can Be Traced?

* LLM Calls
* Retrieval
* Tool Calls
* Agents
* LangGraph Nodes

---

### Q. LangSmith vs Logging?

Logging:

```text
Raw Logs
```

LangSmith:

```text
End-to-End LLM Observability
```

---

## 29. Enterprise GenAI

### Q. Enterprise RAG Architecture?

```text
User
↓
API
↓
Retriever
↓
Vector DB
↓
Reranker
↓
LLM
↓
Answer
```

---

### Q. Why Do Enterprises Prefer RAG?

Benefits:

* Current Knowledge
* Lower Hallucinations
* No Model Retraining

---

### Q. Key Enterprise Requirements?

* Security
* Scalability
* Monitoring
* Evaluation
* Governance

---

### Q. Enterprise Vector Databases?

* Qdrant
* Pinecone
* Weaviate
* Milvus

---

## 30. LLM System Design

### Q. Design a Production RAG System.

Architecture:

```text
User
↓
API
↓
Query Rewriter
↓
Retriever
↓
BM25 + Vector Search
↓
Reranker
↓
Context Builder
↓
LLM
↓
Critic
↓
Answer
```

---

### Q. Design a Multi-Agent System.

Architecture:

```text
Planner
↓
Retriever
↓
Research Agent
↓
Critic Agent
↓
Answer Agent
```

---

### Q. Design a Scalable Enterprise AI Platform.

Components:

```text
Load Balancer
API Gateway
Authentication
RAG Layer
Agent Layer
Vector DB
LLM Provider
Evaluation Layer
Monitoring Layer
```

---
