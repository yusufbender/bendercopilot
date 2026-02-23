from qdrant_client import QdrantClient
from config import settings
from app.utils.logger import get_logger

logger = get_logger()

def get_qdrant_client():
    client = QdrantClient(
        host=settings.QDRANT_HOST,
        port=settings.QDRANT_PORT,
    )
    return client