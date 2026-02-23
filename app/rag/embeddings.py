from sentence_transformers import SentenceTransformer
from app.utils.logger import get_logger

logger = get_logger()

class EmbeddingModel:
    def __init__(self):
        logger.info("Loading embedding model...")
        self.model = SentenceTransformer("BAAI/bge-small-en-v1.5")
        logger.info("Embedding model loaded.")

    def encode(self, texts):
        return self.model.encode(
            texts,
            normalize_embeddings=True
        )

embedding_model = EmbeddingModel()