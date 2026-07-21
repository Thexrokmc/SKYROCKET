from scanner.scanner import Scanner

from engine.sky_score_engine import SkyScoreEngine

from market.market_cycle_engine import MarketCycleEngine

from advisor.ai_advisor import AIAdvisor

from report.report_generator import ReportGenerator

from history.history_manager import HistoryManager

from models.analysis_result import AnalysisResult


class SkyrocketEngine:

    def __init__(self):

        self.scanner = Scanner()

        self.score_engine = SkyScoreEngine()

        self.market_cycle = MarketCycleEngine()

        self.advisor = AIAdvisor()

        self.report = ReportGenerator()

        self.history = HistoryManager()

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

        result = AnalysisResult(

            symbol=symbol,

            price=timeframe_market.price,

            score=score,

            market_cycle=cycle,

            decision=advice[-1],

            reasons=advice

        )

        self.history.save(result)

        report = self.report.generate(

            result.symbol,

            result.market_cycle,

            result.score,

            result.decision,

            result.reasons

        )

        return report
