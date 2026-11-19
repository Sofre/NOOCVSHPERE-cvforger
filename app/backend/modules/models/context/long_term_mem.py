from .base import BaseContext

class Long_TermMemoryContext(BaseContext):
    def build(self) -> dict:
        if not self.validate():
            raise ValueError("Invalid long-term memory context")
        return {
            "type": "long-term",
            "content": self.to_dict(),
        }

longmem = Long_TermMemoryContext(
    {
        "user_profile": {
            "personal_information": {},
            "professional_background": {},
            "education": {},
            "experience": [],
            "skills": [],
            "certifications": [],
        },
        "career_preferences": {
            "preferred_job_titles": [],
            "preferred_locations": [],
            "employment_types": [],
            "salary_expectations": {},
            "remote_preference": None,
            "preferred_technologies": [],
        },
        "career_goals": [],
        "user_preferences": {
            "cv_formatting": {},
            "communication_style": {},
            "other_preferences": {},
        },
        "persistent_decisions": [],
        "updated_at": None,
    }
)