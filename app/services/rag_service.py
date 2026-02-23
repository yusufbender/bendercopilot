from typing import List, Dict, Any
from app.rag.indexer import index_text as _index_text
from app.rag.indexer import search_text as _search_text
from app.utils.logger import get_logger

logger = get_logger()


class RAGService:
    """
    Application service layer for Retrieval operations.

    Responsibilities:
    - Orchestrate indexing
    - Orchestrate semantic search
    - Build structured response payloads
    - Prepare context for future LLM usage
    """

    def __init__(self):
        logger.info("RAGService initialized")

    # -------------------------
    # INDEXING
    # -------------------------
    def index(self, text: str, metadata: Dict[str, Any] | None = None) -> Dict[str, str]:
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")

        metadata = metadata or {"source": "unknown"}

        logger.info("Indexing document...")
        _index_text(text, metadata)

        return {"status": "indexed"}

    # -------------------------
    # SEARCH
    # -------------------------
    def search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        if not query or not query.strip():
            raise ValueError("Query cannot be empty")

        logger.info(f"Searching for query: {query}")

        results = _search_text(query, limit=limit)

        # Normalize response structure
        formatted = [
            {
                "id": r["id"],
                "score": r["score"],
                "metadata": r.get("payload", {}),
            }
            for r in results
        ]

        return formatted

    # -------------------------
    # CONTEXT BUILDER
    # (Future LLM integration)
    # -------------------------
    def build_context(self, query: str, limit: int = 5) -> str:
        """
        Returns concatenated context string for LLM usage.
        """
        results = self.search(query, limit)

        if not results:
            return ""

        context_blocks = []
        for r in results:
            meta = r["metadata"]
            context_blocks.append(str(meta))

        return "\n".join(context_blocks)