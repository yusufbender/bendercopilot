# 🚀 BenderCopilot v0.1 – Core RAG Backend

Minimal, production-ready Retrieval-Augmented Generation (RAG) backend  
for a future multi-agent IDE Copilot system.

This is the foundational layer of a modular AI engineering platform.

---

## 🧠 Vision

BenderCopilot aims to evolve into a multi-agent AI IDE assistant capable of:

- Context-aware code understanding  
- Intelligent refactoring suggestions  
- Test generation  
- Documentation synthesis  
- Agent collaboration  

v0.1 focuses purely on the semantic retrieval layer.

---

## 🏗 Architecture

Client  
↓  
FastAPI Service  
↓  
Embedding Model (BAAI/bge-small-en-v1.5)  
↓  
Qdrant Vector Database  
↓  
Cosine Similarity Search  

---

## ⚙ Tech Stack

- **FastAPI** – API layer  
- **Qdrant** – Vector database  
- **Sentence-Transformers**  
- **BAAI/bge-small-en-v1.5**  
- **Docker Compose**  
- **Python 3.12**

---

## 📦 Features (v0.1)

- Semantic text indexing  
- Cosine similarity vector search  
- Persistent Qdrant collection  
- JSON-safe API responses  
- Dockerized vector DB setup  

---

## ▶ Run Locally

```bash
docker compose up -d
python -m uvicorn main:app --reload
```

---

## 🔌 API Endpoints

### Index Text
```http
POST /index
```

### Search
```http
GET /search?q=your_query
```

### Test Embedding
```http
GET /embed?q=test
```

---

## 📈 Roadmap

### v0.2
- Multi-agent orchestrator (LangGraph / AutoGen)  
- Tool-based retrieval integration  

### v0.3
- AST-based semantic chunking (Tree-sitter)  
- Metadata-enriched indexing  

### v0.4
- VSCode extension integration  
- Interactive Copilot UI  

---

## 📌 Project Status

Actively evolving.  
Part of a broader AI Engineering portfolio.

---

## 🛠 Author

Yusuf – AI/ML & DevOps Engineer  
Building modular AI systems with production discipline.