from abc import ABC, abstractmethod
from typing import Any


class BaseContext(ABC):
    def __init__(self, content: dict[str, Any]) -> None:
        self.content = content
    # Builds the context - abstract method it doesnt have a role it supposed to be overriden
    @abstractmethod
    def build(self) -> dict[str, Any]:
        pass
    # Validate the context exists
    def validate(self) -> bool:
        return bool(self.content)
    # Returns the content as a dict
    def to_dict(self) -> dict[str, Any]:
        return self.content