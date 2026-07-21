from data.data_provider import DataProvider
from data.timeframe_market import TimeframeMarket


class MultiTimeframeProvider:

    def __init__(self):

        self.provider = DataProvider()

    def load(
        self,
        symbol: str
    ) -> TimeframeMarket:

        market = TimeframeMarket()

        market.daily = self.provider.load_market_data(
            symbol=symbol,
            interval="1d"
        )

        market.h4 = self.provider.load_market_data(
            symbol=symbol,
            interval="4h"
        )

        market.h1 = self.provider.load_market_data(
            symbol=symbol,
            interval="1h"
        )

        market.m15 = self.provider.load_market_data(
            symbol=symbol,
            interval="15m"
        )

        return market
