from .base import BaseContext

class Short_TermMemoryContext(BaseContext):
    def build(self) -> dict:
        if not self.validate():
            raise ValueError("Invalid short-term memory context")
        return {
            "type": "short-term",
            "content": self.to_dict(),
        }

shortmem = Short_TermMemoryContext(
    {
        "current_goal": None,
        "active_task": None,
        "status_active_task": False,
        "recent_decisions": [],
        "temporary_facts": [],
    }
)