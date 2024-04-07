from abc import abstractmethod


class Animal:
    @abstractmethod
    def eat(self, food: str) -> None: ...
