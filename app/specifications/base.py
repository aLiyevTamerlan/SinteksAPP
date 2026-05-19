from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")

class Specification(ABC, Generic[T]):
    @abstractmethod
    async def is_satisfied(self, ctx: T) -> bool:
        pass

    def exception(self, ctx: T) -> None:
        return None