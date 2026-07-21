from data.market import MarketData
from data.kraken_client import KrakenClient
from indicators.technical_indicators import TechnicalIndicators


class DataProvider:

    def __init__(self):

        self.client = KrakenClient()

    def load_market_data(
        self,
        symbol: str = "PF_XBTUSD",
        interval: str = "1h"
    ) -> MarketData:

        market = MarketData()

        data = self.client.get_candles(
            symbol=symbol,
            interval=interval
        )

        closes = []

        if "candles" in data:

            for candle in data["candles"]:

                closes.append(
                    float(candle["close"])
                )

        if len(closes) == 0:
            return market

        market.symbol = symbol

        market.price = closes[-1]

        market.ema50 = TechnicalIndicators.ema(
            closes,
            50
        )

        market.ema200 = TechnicalIndicators.ema(
            closes,
            200
        )

        market.rsi = TechnicalIndicators.rsi(
            closes
        )

        (
            market.macd,
            market.macd_signal,
            market.macd_histogram
        ) = TechnicalIndicators.macd(
            closes
        )

        return market
