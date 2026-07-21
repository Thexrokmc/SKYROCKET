from rules.base_rule import BaseRule
from rules.rule_result import RuleResult
from data.fact_ids import MACD_BULLISH


class MACDBullishRule(BaseRule):

    def __init__(self):
        super().__init__(
            name="MACD Bullish",
            weight=15
        )

    def evaluate(self, facts: dict) -> RuleResult:
        passed = facts.get(
            MACD_BULLISH,
            False
        )

        return RuleResult(
            name=self.name,
            passed=passed,
            weight=self.weight
        )
