from rules.base_rule import BaseRule
from rules.rule_result import RuleResult

from data.fact_ids import (
    RSI_BULLISH,
    MACD_BULLISH,
)


class MomentumRule(BaseRule):

    def __init__(self):

        super().__init__(
            name="Momentum Rule",
            weight=20
        )

    def evaluate(self, facts: dict) -> RuleResult:

        passed = (
            facts.get(
                RSI_BULLISH,
                False
            )
            and
            facts.get(
                MACD_BULLISH,
                False
            )
        )

        return RuleResult(
            name=self.name,
            passed=passed,
            weight=self.weight,
            description="RSI and MACD confirm bullish momentum"
        )
