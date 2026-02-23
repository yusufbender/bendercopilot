from qdrant_client.models import Distance, VectorParams
from app.rag.qdrant_client import get_qdrant_client
from app.utils.logger import get_logger

logger = get_logger()

COLLECTION_NAME = "codebase"
VECTOR_SIZE = 384

def create_collection():
    client = get_qdrant_client()

    collections = client.get_collections().collections
    names = [c.name for c in collections]

    if COLLECTION_NAME not in names:
        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=VECTOR_SIZE,
                distance=Distance.COSINE
            )
        )
        logger.info(f"Collection '{COLLECTION_NAME}' created.")
    else:
        logger.info(f"Collection '{COLLECTION_NAME}' already exists.")