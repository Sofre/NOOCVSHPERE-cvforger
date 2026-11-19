
from .base import BaseContext

class MemoryContext(BaseContext):

    def __init__(
        self,
        content: dict,
        short_term,
        long_term,
        semantic
    ):
        super().__init__(content)

        self.short_term = short_term
        self.long_term = long_term
        self.semantic = semantic

    def build(self):

        if not self.validate():
            raise ValueError("Invalid memory context")

        return {
            "type": "memory",
            "content": {
                "short_term": self.short_term.build(),
                "long_term": self.long_term.build(),
                "semantic": self.semantic.build()
            }
        }
