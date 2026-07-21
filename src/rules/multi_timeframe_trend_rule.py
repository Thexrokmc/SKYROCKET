from rules.base_rule import BaseRule
from rules.rule_result import RuleResult


class MultiTimeframeTrendRule(BaseRule):

    def __init__(self):

        super().__init__(
            name="Multi-Timeframe Trend",
            weight=30
        )

    def evaluate(self, timeframe_market) -> RuleResult:

        passed = (

            timeframe_market.daily.price >
            timeframe_market.daily.ema200

            and

            timeframe_market.h4.price >
            timeframe_market.h4.ema200

            and

            timeframe_market.h1.price >
            timeframe_market.h1.ema200

        )

        return RuleResult(
            name=self.name,
            passed=passed,
            weight=self.weight,
            description="Daily, H4 and H1 are above EMA200"
        )
