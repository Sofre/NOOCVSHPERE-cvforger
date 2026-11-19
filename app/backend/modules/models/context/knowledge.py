from .base import BaseContext

class KnowledgeContext(BaseContext):
    
    def __init__(self,content:dict):
        super().__init__(content)

    def build(self):

        if not self.validate():
            raise ValueError("Invalid value")

        return ({

            "type:" "knowledge",
            "content" : self.to_dist()
            
            })


knowledge = KnowledgeContext({

    "candidate": {
        "profile": None,
        "cv": None,
        "skills": [],
        "experience": [],
        "education": [],
        "projects": [],
        "certifications": []
    },

    "job": {
        "job_id": None,
        "title": None,
        "company": None,
        "description": None,
        "requirements": [],
        "responsibilities": [],
        "technologies": []
    },

    "company": {
        "name": None,
        "description": None,
        "industry": None,
        "website": None
    },

    "references": []
})






