from fastapi import FastAPI
from app.utils.logger import get_logger
from config import settings
from app.rag.embeddings import embedding_model
from pydantic import BaseModel
from app.services.rag_service import RAGService

rag_service = RAGService()
class IndexRequest(BaseModel):
    text: str


logger = get_logger()

app = FastAPI(title=settings.PROJECT_NAME)

from app.rag.collections import create_collection

@app.on_event("startup")
async def startup():
    logger.info("Application started")
    create_collection()
@app.get("/")
def root():
    logger.info("Health check called")
    return {"status": "running"}

@app.get("/embed")
def embed_test(q: str):
    vector = embedding_model.encode([q])[0]
    return {
        "dim": len(vector),
        "sample": vector[:5]
    }

from app.rag.indexer import index_text, search_text

@app.post("/index")
def index_endpoint(req: IndexRequest):
    return rag_service.index(req.text, {"source": "manual_test"})


@app.get("/search")
def search_endpoint(q: str, limit: int = 5):
    return {"results": rag_service.search(q, limit)}

from app.orchestrator.copilot_orchestrator import CopilotOrchestrator

orchestrator = CopilotOrchestrator()

@app.get("/ask")
def ask_endpoint(q: str):
    return orchestrator.handle_query(q)