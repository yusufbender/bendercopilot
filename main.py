from fastapi import FastAPI
from app.utils.logger import get_logger
from config import settings
from app.rag.embeddings import embedding_model
from pydantic import BaseModel

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
    metadata = {"source": "manual_test"}
    index_text(req.text, metadata)
    return {"status": "indexed"}

@app.get("/search")
def search_endpoint(q: str):
    results = search_text(q)
    return {"results": results}