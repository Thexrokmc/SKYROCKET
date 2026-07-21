from rules.base_rule import BaseRule
from rules.rule_result import RuleResult
from data.fact_ids import RSI_OVERSOLD


class RSIOversoldRule(BaseRule):

    def __init__(self):
        super().__init__(
            name="RSI Oversold",
            weight=15
        )

    def evaluate(self, facts: dict) -> RuleResult:
        passed = facts.get(
            RSI_OVERSOLD,
            False
        )

        return RuleResult(
            name=self.name,
            passed=passed,
            weight=self.weight
        )
