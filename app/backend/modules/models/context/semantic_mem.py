from .base import BaseContext

class Semantic_MemoryContext(BaseContext):
    def build(self) -> dict:
        if not self.validate():
            raise ValueError("Invalid semantic memory context")
        return {
            "type": "semantic",
            "content": self.to_dict(),
        }

semantic_memory = Semantic_MemoryContext(
    {
        "documents": {
            "cv_documents": [],
            "job_listings": [],
            "certificates": [],
            "research_papers": [],
            "project_documents": [],
        },
        "knowledge_chunks": [],
        "embeddings": {
            "model": None,
            "vector_dimension": None,
        },
        "metadata": {
            "source": None,
            "document_id": None,
            "chunk_id": None,
            "created_at": None,
        },
    }
)
