from app.services.rag_service import RAGService
from app.utils.logger import get_logger

logger = get_logger()


class CopilotOrchestrator:

    def __init__(self):
        self.rag_service = RAGService()
        logger.info("CopilotOrchestrator initialized")

    def handle_query(self, query: str) -> dict:
        if not query.strip():
            raise ValueError("Query cannot be empty")

        # 1️⃣ Retrieval
        context = self.rag_service.build_context(query)

        # 2️⃣ LLM Stub (temporary)
        answer = self._mock_llm(query, context)

        return {
            "query": query,
            "context_used": context,
            "answer": answer
        }

    def _mock_llm(self, query: str, context: str) -> str:
        return f"[MOCK RESPONSE]\nQuery: {query}\nContext: {context}"