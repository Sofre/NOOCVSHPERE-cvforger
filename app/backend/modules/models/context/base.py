from abc import ABC, abstractmethod
from typing import Any


class BaseContext(ABC):
    def __init__(self, content: dict[str, Any]) -> None:
        self.content = content

    @abstractmethod
    def build(self) -> dict[str, Any]:
        pass

    def validate(self) -> bool:
        return bool(self.content)

    def to_dict(self) -> dict[str, Any]:
        return self.content