
from typing import Any

from .base import BaseContext


class MemoryContext(BaseContext):
    def __init__(
        self,
        content: dict[str, Any],
        short_term: BaseContext,
        long_term: BaseContext,
        semantic: BaseContext,
    ) -> None:
        super().__init__(content)
        if not all(
            isinstance(context, BaseContext)
            for context in (short_term, long_term, semantic)
        ):
            raise TypeError("Memory components must be BaseContext instances")
        self.short_term = short_term
        self.long_term = long_term
        self.semantic = semantic

    def build(self) -> dict[str, Any]:
        if not self.validate():
            raise ValueError("Invalid memory context")

        return {
            "type": "memory",
            "content": {
                "short_term": self.short_term.build(),
                "long_term": self.long_term.build(),
                "semantic": self.semantic.build(),
            },
        }
