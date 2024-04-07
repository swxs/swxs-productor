from typing import runtime_checkable, Protocol
from abc import abstractmethod


@runtime_checkable
class Animal(Protocol):
    @abstractmethod
    def eat(self, food: str) -> None: ...
