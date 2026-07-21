from dataclasses import dataclass
from typing import Dict, List

from indicators.ema import EMA
from indicators.rsi import RSI
from indicators.macd import MACD


@dataclass
class IndicatorResult:

    ema20: float
    ema50: float
    ema200: float
    rsi14: float

    macd: float
    macd_signal: float
    macd_histogram: float


class IndicatorEngine:

    def __init__(self, logger):

        self.logger = logger

    def calculate(self, candles: List[dict]) -> IndicatorResult:

        closes = [

            float(c["close"])

            for c in candles

        ]

        ema20 = EMA(20).calculate(closes)

        ema50 = EMA(50).calculate(closes)

        ema200 = EMA(200).calculate(closes)

        rsi14 = RSI(14).calculate(closes)

        macd = MACD().calculate(closes)

        return IndicatorResult(

            ema20=ema20,

            ema50=ema50,

            ema200=ema200,

            rsi14=rsi14,

            macd=macd.macd,

            macd_signal=macd.signal,

            macd_histogram=macd.histogram

        )

    def calculate_all(

        self,

        market_data: Dict

    ):

        result = {}

        for symbol in market_data:

            result[symbol] = {}

            for timeframe in market_data[symbol]:

                snapshot = market_data[symbol][timeframe]

                self.logger.info(

                    "Calculating indicators %s %s",

                    symbol,

                    timeframe

                )

                result[symbol][timeframe] = self.calculate(

                    snapshot.candles

                )

        return result
