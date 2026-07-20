from abc import ABC, abstractmethod
from rules.rule_result import RuleResult


class BaseRule(ABC):

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    @abstractmethod
    def evaluate(self, facts: dict) -> RuleResult:
        pass
