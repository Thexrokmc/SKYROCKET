from .base_rule import BaseRule
from .rule_result import RuleResult


class AllocationRule(BaseRule):

    def __init__(self):
        super().__init__(
            name="Portfolio Allocation",
            weight=15
        )

    def evaluate(self, facts: dict) -> RuleResult:

        return RuleResult(
            name=self.name,
            passed=True,
            weight=self.weight
        )
