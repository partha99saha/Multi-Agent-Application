# LLM Engineering Interview Questions & Answers (Part 1)

## 1. NLP Fundamentals

### Q. What is NLP?

Natural Language Processing (NLP) is the field of AI that enables computers to understand, process, generate, and interact with human language.

**Libraries:**

* NLTK
* spaCy
* Gensim
* Hugging Face Transformers

---

### Q. What is Tokenization?

Tokenization is the process of breaking text into smaller units called tokens.

Example:

```text
AWS S3 stores data
```

Tokens:

```text
["AWS", "S3", "stores", "data"]
```

Modern LLMs use subword tokenization:

```text
internationalization
→ inter + national + ization
```

**Libraries:**

* tiktoken
* sentencepiece
* transformers tokenizer

---

### Q. What is Stemming vs Lemmatization?

**Stemming**

```text
running → run
studies → studi
```

Fast but less accurate.

**Lemmatization**

```text
running → run
better → good
```

Uses linguistic knowledge.

**Libraries:**

* NLTK
* spaCy

---

### Q. What are Stop Words?

Common words with little semantic meaning.

Examples:

```text
the
a
is
of
```

Usually removed in traditional retrieval systems.

---

## 2. Transformers

### Q. Why were Transformers introduced?

RNNs and LSTMs struggled with:

* Long-range dependencies
* Sequential processing
* Slow training

Transformers introduced:

```text
Self-Attention
Parallel Processing
Scalability
```

Paper:

```text
Attention Is All You Need (2017)
```

---

### Q. What is Self-Attention?

Self-attention allows a token to attend to all other tokens in a sequence.

Example:

```text
AWS stores data in S3.
```

"S3" receives attention from:

```text
AWS
stores
data
```

to understand context.

---

### Q. What are Query, Key, and Value?

For every token:

```text
Query (Q)
Key (K)
Value (V)
```

Attention score:

```text
Attention(Q,K,V)
=
softmax(QKᵀ/√d)V
```

This determines which tokens are important.

---

### Q. What is Multi-Head Attention?

Multiple attention mechanisms run in parallel.

Benefits:

* Captures different relationships
* Improves context understanding
* Better language modeling

---

## 3. LLM Fundamentals

### Q. What is a Large Language Model?

A neural network trained on massive text corpora to predict the next token.

Examples:

* GPT-4o
* Claude
* Gemini
* Llama

---

### Q. How does an LLM generate text?

Process:

```text
Prompt
↓
Tokenization
↓
Transformer Layers
↓
Probability Distribution
↓
Next Token
↓
Repeat
```

---

### Q. What are Temperature and Top-P?

Temperature controls randomness.

```text
0.0 → deterministic
1.0 → balanced
2.0 → creative
```

Top-P selects tokens from cumulative probability mass.

---

### Q. What causes Hallucinations?

Reasons:

* Missing knowledge
* Ambiguous prompts
* Weak retrieval
* Training limitations

---

## 4. Prompt Engineering

### Q. What is Prompt Engineering?

Designing prompts to improve LLM outputs.

Goal:

```text
Accuracy
Consistency
Structured Output
Reduced Hallucinations
```

---

### Q. What is Zero-Shot Prompting?

No examples provided.

Example:

```text
Explain AWS S3.
```

---

### Q. What is Few-Shot Prompting?

Provide examples.

Example:

```text
Input: EC2
Output: Compute Service

Input: S3
Output: Storage Service
```

---

### Q. What is Chain-of-Thought Prompting?

The model reasons step by step.

Example:

```text
Think step by step before answering.
```

Useful for:

* Math
* Logic
* Planning

---

### Q. What is Self-Consistency?

Generate multiple reasoning paths.

Choose the most common answer.

Improves reasoning reliability.

---

### Q. What is Tree-of-Thought?

Instead of one reasoning path:

```text
Idea A
Idea B
Idea C
```

Explore multiple reasoning branches before deciding.

---

### Q. What is Structured Output Generation?

Force responses into formats such as:

```json
{
  "name": "",
  "skills": []
}
```

Useful for APIs and automation.

---

## 5. Context Engineering

### Q. What is Context Engineering?

Managing what information is sent to the LLM.

Includes:

* Prompt construction
* Retrieval
* Memory
* Context compression

---

### Q. What is Context Window?

Maximum tokens an LLM can process.

Example:

```text
128K tokens
200K tokens
1M tokens
```

depending on model.

---

### Q. What is Lost-in-the-Middle?

Models often focus on:

```text
Beginning
End
```

while missing important information in the middle.

---

### Q. Long Context vs RAG?

**Long Context**

Pros:

* Simpler

Cons:

* Expensive
* Slow

**RAG**

Pros:

* Cheap
* Scalable

Cons:

* Retrieval quality matters

---

## 6. Embeddings

### Q. What are Embeddings?

Dense vector representations of text.

Example:

```text
AWS S3
[0.12, -0.41, 0.78 ...]
```

Semantically similar text has similar vectors.

---

### Q. Why are Embeddings Important?

Used for:

* Search
* RAG
* Recommendations
* Clustering

---

### Q. Difference Between Keyword Search and Embeddings?

Keyword:

```text
Exact matching
```

Embedding:

```text
Semantic matching
```

---

### Q. What Embedding Models Are Common?

Examples:

* OpenAI Embeddings
* BGE
* E5
* Instructor
* Sentence Transformers

Libraries:

* sentence-transformers
* transformers

---

## 7. Chunking

### Q. Why Chunk Documents?

LLMs cannot process huge documents efficiently.

Chunking splits content into smaller pieces.

---

### Q. Common Chunking Strategies?

1. Fixed Size
2. Recursive Chunking
3. Semantic Chunking
4. Hierarchical Chunking

---

### Q. What is Chunk Overlap?

Overlap preserves context.

Example:

```text
Chunk 1: 1-500
Chunk 2: 450-950
```

---

## 8. Vector Databases

### Q. Why Use Vector Databases?

Store embeddings and perform similarity search.

Examples:

* Qdrant
* Pinecone
* Weaviate
* Milvus
* Chroma

---

### Q. What is Similarity Search?

Find nearest vectors using:

* Cosine Similarity
* Dot Product
* Euclidean Distance

---

### Q. Why is Qdrant Popular?

Features:

* Fast retrieval
* Filtering
* Metadata support
* Open source

---

## 9. Retrieval

### Q. What is Retrieval in RAG?

Finding relevant documents before generation.

Flow:

```text
Query
↓
Retriever
↓
Relevant Chunks
↓
LLM
```

---

### Q. What is Dense Retrieval?

Embedding-based retrieval.

Semantic understanding.

---

### Q. What is Sparse Retrieval?

Keyword-based retrieval.

Example:

```text
BM25
TF-IDF
```

---

## 10. Hybrid Search

### Q. What is Hybrid Search?

Combines:

```text
BM25
+
Vector Search
```

Benefits:

* Better recall
* Better precision

---

### Q. Why Use Hybrid Retrieval?

Captures:

```text
Exact Keywords
+
Semantic Meaning
```

---

## 11. Reranking

### Q. What is Reranking?

Second-stage ranking.

Process:

```text
Retriever
↓
Top 20
↓
Reranker
↓
Top 5
```

---

### Q. Why Use a Reranker?

Improves context quality.

Reduces irrelevant chunks.

---

### Q. Common Reranker Models?

Examples:

* BGE Reranker
* Cohere Rerank
* Cross Encoder

Libraries:

```python
sentence-transformers
FlagEmbedding
```

---

## 12. Advanced RAG

### Q. What is RAG?

Retrieval-Augmented Generation combines:

```text
Knowledge Retrieval
+
LLM Generation
```

---

### Q. What are the Main RAG Components?

```text
Embedding Model
Retriever
Vector Database
Reranker
Prompt Builder
LLM
```

---

### Q. What is Query Rewriting?

Transforms:

```text
What is S3?
```

into

```text
Explain AWS S3 cloud storage service.
```

Improves retrieval.

---

### Q. What is Context Compression?

Reduce retrieved content while preserving important information.

Benefits:

* Lower cost
* Faster inference

---

### Q. What Metrics Evaluate RAG?

* Context Precision
* Context Recall
* Faithfulness
* Answer Relevance

Libraries:

* Ragas
* DeepEval
* LangSmith

---

## 13. Hallucinations

### Q. What is Hallucination?

When an LLM generates information not grounded in facts.

---

### Q. Can RAG Eliminate Hallucinations?

No.

It reduces hallucinations but does not completely eliminate them.

---

### Q. How Can Hallucinations Be Reduced?

Methods:

* Better retrieval
* Better reranking
* Better prompts
* Verification layers
* Citations
* Evaluations

---

## 14. Tool Calling

### Q. What is Tool Calling?

LLMs invoke external functions.

Example:

```text
Weather API
Calculator
Database Query
Search Engine
```

---

### Q. Why Use Tool Calling?

LLMs cannot reliably:

* Calculate large numbers
* Access real-time data
* Execute code

Tools solve these limitations.

---

### Q. Function Calling vs Tool Calling?

Function Calling:

```text
Model calls predefined functions.
```

Tool Calling:

```text
Broader concept including APIs and services.
```

---

## 15. MCP (Model Context Protocol)

### Q. What is MCP?

Model Context Protocol standardizes how models interact with tools and external systems.

---

### Q. Why Was MCP Introduced?

Before MCP:

```text
Custom Integrations
Custom APIs
Custom Tool Definitions
```

After MCP:

```text
Standard Interface
```

for tools and resources.

---

### Q. MCP vs Function Calling?

Function Calling:

```text
Model-specific
```

MCP:

```text
Vendor-neutral protocol
```

---

### Q. Benefits of MCP?

* Standardization
* Reusability
* Tool portability
* Better interoperability

Frameworks:

* MCP Python SDK
* Claude MCP
* OpenAI MCP Integrations
