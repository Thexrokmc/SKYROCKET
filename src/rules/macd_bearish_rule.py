from rules.base_rule import BaseRule
from rules.rule_result import RuleResult
from data.fact_ids import MACD_BEARISH


class MACDBearishRule(BaseRule):

    def __init__(self):
        super().__init__(
            name="MACD Bearish",
            weight=15
        )

    def evaluate(self, facts: dict) -> RuleResult:
        passed = facts.get(
            MACD_BEARISH,
            False
        )

        return RuleResult(
            name=self.name,
            passed=passed,
            weight=self.weight
        )
