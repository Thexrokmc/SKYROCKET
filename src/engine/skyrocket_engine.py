from scanner.scanner import Scanner

from engine.sky_score_engine import SkyScoreEngine

from market.market_cycle_engine import MarketCycleEngine

from advisor.ai_advisor import AIAdvisor

from report.report_generator import ReportGenerator


class SkyrocketEngine:

    def __init__(self):

        self.scanner = Scanner()

        self.score_engine = SkyScoreEngine()

        self.market_cycle = MarketCycleEngine()

        self.advisor = AIAdvisor()

        self.report = ReportGenerator()

    def analyze(self, symbol):

        timeframe_market = self.scanner.scan(symbol)

        score = self.score_engine.calculate(
            timeframe_market.rule_results
        )

        cycle = self.market_cycle.detect(

            timeframe_market.price,

            timeframe_market.ema200,

            timeframe_market.rsi,

            timeframe_market.macd

        )

        advice = self.advisor.advise(

            cycle,

            score,

            "AUTO",

            "AUTO",

            "AUTO"

        )

        report = self.report.generate(

            symbol,

            cycle,

            score,

            advice[-1],

            advice

        )

        return report
