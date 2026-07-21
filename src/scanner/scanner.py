from data.multi_timeframe_provider import MultiTimeframeProvider

from rules.multi_timeframe_trend_rule import (
    MultiTimeframeTrendRule
)

from rules.multi_timeframe_momentum_rule import (
    MultiTimeframeMomentumRule
)

from decision.sky_score_engine import (
    SkyScoreEngine
)


class Scanner:

    def __init__(self):

        self.provider = MultiTimeframeProvider()

        self.rules = [

            MultiTimeframeTrendRule(),

            MultiTimeframeMomentumRule(),

        ]

        self.sky_score = SkyScoreEngine()

    def analyze(self, symbol):

        market = self.provider.load(symbol)

        results = []

        for rule in self.rules:

            results.append(
                rule.evaluate(market)
            )

        score = self.sky_score.calculate(
            results
        )

        return {

            "symbol": symbol,

            "score": score,

            "results": results

        }
