import uuid
from app.rag.qdrant_client import get_qdrant_client
from app.rag.embeddings import embedding_model
from app.rag.collections import COLLECTION_NAME
from app.utils.logger import get_logger

logger = get_logger()

def index_text(text: str, metadata: dict):
    client = get_qdrant_client()

    vector = embedding_model.encode([text])[0]

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            {
                "id": str(uuid.uuid4()),
                "vector": vector.tolist(),
                "payload": metadata
            }
        ]
    )

    logger.info("Document indexed successfully.")

def search_text(query: str, limit: int = 3):
    client = get_qdrant_client()

    query_vector = embedding_model.encode([query])[0]

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector.tolist(),
        limit=limit
    )

    return [
        {
            "id": r.id,
            "score": r.score,
            "payload": r.payload
        }
        for r in response.points
    ]