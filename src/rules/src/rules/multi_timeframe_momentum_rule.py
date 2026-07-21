from rules.base_rule import BaseRule
from rules.rule_result import RuleResult


class MultiTimeframeMomentumRule(BaseRule):

    def __init__(self):

        super().__init__(
            name="Multi-Timeframe Momentum",
            weight=30
        )

    def evaluate(self, timeframe_market) -> RuleResult:

        passed = (

            timeframe_market.daily.macd >
            timeframe_market.daily.macd_signal

            and

            timeframe_market.h4.macd >
            timeframe_market.h4.macd_signal

            and

            timeframe_market.h1.macd >
            timeframe_market.h1.macd_signal

            and

            timeframe_market.daily.rsi > 50

            and

            timeframe_market.h4.rsi > 50

            and

            timeframe_market.h1.rsi > 50

        )

        return RuleResult(
            name=self.name,
            passed=passed,
            weight=self.weight,
            description="Momentum is bullish on Daily, H4 and H1"
        )
