from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Any


@dataclass
class MarketSnapshot:
    symbol: str
    timeframe: str
    timestamp: datetime
    candles: List[Dict[str, Any]]


class MarketDataEngine:
    """
    Coordinates market data retrieval from the configured provider.
    """

    def __init__(self, provider, logger):

        self.provider = provider
        self.logger = logger

    def load(
        self,
        symbols: List[str],
        timeframes: List[str]
    ) -> Dict[str, Dict[str, MarketSnapshot]]:

        result = {}

        for symbol in symbols:

            self.logger.info(
                "Loading market data for %s",
                symbol
            )

            result[symbol] = {}

            for timeframe in timeframes:

                candles = self.provider.get_candles(
                    symbol=symbol,
                    timeframe=timeframe
                )

                result[symbol][timeframe] = MarketSnapshot(

                    symbol=symbol,

                    timeframe=timeframe,

                    timestamp=datetime.utcnow(),

                    candles=candles

                )

        return result
