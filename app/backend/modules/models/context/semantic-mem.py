from .base import BaseContext

class Semantic_MemoryContext(BaseContext):

    def __init__(self,content:dict):
        super().__init__(content)

    def build(self) -> dict:

        if not self.validate():
            raise ValueError("Invalid system context")

        
        return {

            "type": "semantic", # short-term should be added to the memory context of the chatbot and feed in the long-term for the agents ? 
            "content": self.to_dict()
        }

# Semantic search of persistent data and facts 
semantic_memory = {
    "documents": {
        "cv_documents": [],
        "job_listings": [],
        "certificates": [],
        "research_papers": [],
        "project_documents": []
    },

    "knowledge_chunks": [],

    "embeddings": {
        "model": None,
        "vector_dimension": None
    },

    "metadata": {
        "source": None,
        "document_id": None,
        "chunk_id": None,
        "created_at": None
    }
}
