from .base import BaseContext


class KnowledgeContext(BaseContext):
    def build(self) -> dict:
        if not self.validate():
            raise ValueError("Invalid knowledge context")
        return {
            "type": "knowledge",
            "content": self.to_dict(),
        }


knowledge = KnowledgeContext(
    {
        "candidate": {
            "profile": None,
            "cv": None,
            "skills": [],
            "experience": [],
            "education": [],
            "projects": [],
            "certifications": [],
        },
        "job": {
            "job_id": None,
            "title": None,
            "company": None,
            "description": None,
            "requirements": [],
            "responsibilities": [],
            "technologies": [],
        },
        "company": {
            "name": None,
            "description": None,
            "industry": None,
            "website": None,
        },
        "references": [],
    }
)

