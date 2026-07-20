from abc import ABC, abstractmethod


class BaseRule(ABC):

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    @abstractmethod
    def evaluate(self, facts: dict) -> bool:
        pass
