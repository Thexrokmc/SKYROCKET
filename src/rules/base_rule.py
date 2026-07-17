from abc import ABC, abstractmethod


class BaseRule(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @abstractmethod
    def evaluate(self, portfolio, market):
        """
        Returns:
        {
            "passed": bool,
            "score": int,
            "reason": str
        }
        """
        pass
