from dataclasses import dataclass
from typing import Dict


@dataclass
class MarketFacts:

    price_above_ema20: bool
    price_above_ema50: bool
    price_above_ema200: bool

    ema20_above_ema50: bool
    ema50_above_ema200: bool

    macd_bullish: bool
    macd_bearish: bool

    rsi_overbought: bool
    rsi_oversold: bool

    trend: str


class FactsEngine:

    def __init__(self, logger):

        self.logger = logger

    def build(self, price, indicators):

        trend = "RANGE"

        if (
            indicators.ema20 > indicators.ema50
            and indicators.ema50 > indicators.ema200
        ):
            trend = "BULL"

        elif (
            indicators.ema20 < indicators.ema50
            and indicators.ema50 < indicators.ema200
        ):
            trend = "BEAR"

        return MarketFacts(

            price_above_ema20=price > indicators.ema20,

            price_above_ema50=price > indicators.ema50,

            price_above_ema200=price > indicators.ema200,

            ema20_above_ema50=(
                indicators.ema20 > indicators.ema50
            ),

            ema50_above_ema200=(
                indicators.ema50 > indicators.ema200
            ),

            macd_bullish=(
                indicators.macd > indicators.macd_signal
            ),

            macd_bearish=(
                indicators.macd < indicators.macd_signal
            ),

            rsi_overbought=(
                indicators.rsi14 >= 70
            ),

            rsi_oversold=(
                indicators.rsi14 <= 30
            ),

            trend=trend

        )

    def build_all(

        self,

        market_data: Dict,

        indicators: Dict

    ):

        facts = {}

        for symbol in market_data:

            facts[symbol] = {}

            for timeframe in market_data[symbol]:

                snapshot = market_data[symbol][timeframe]

                last_price = float(

                    snapshot.candles[-1]["close"]

                )

                facts[symbol][timeframe] = self.build(

                    last_price,

                    indicators[symbol][timeframe]

                )

        return facts
