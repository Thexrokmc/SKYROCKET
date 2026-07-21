from rules.base_rule import BaseRule
from rules.rule_result import RuleResult

from data.fact_ids import (
    PRICE_ABOVE_EMA50
)


class PriceAboveEMA50Rule(BaseRule):

    def __init__(self):

        super().__init__(
            name="Price Above EMA50",
            weight=15
        )

    def evaluate(self, facts: dict) -> RuleResult:

        passed = facts.get(
            PRICE_ABOVE_EMA50,
            False
        )

        return RuleResult(
            name=self.name,
            passed=passed,
            weight=self.weight,
            description="Price is above EMA50"
        )
