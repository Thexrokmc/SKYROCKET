from data.market import MarketData
from data.kraken_client import KrakenClient


class DataProvider:

    def __init__(self):
        self.client = KrakenClient()

    def load_market_data(
        self,
        symbol: str = "PF_XBTUSD"
    ) -> MarketData:

        market = MarketData()

        data = self.client.get_candles(
            symbol=symbol,
            interval="1h"
        )

        market.symbol = symbol

        # TODO:
        # Στο επόμενο βήμα θα κάνουμε parse το JSON
        # και θα γεμίσουμε:
        # market.price
        # market.ema50
        # market.ema200
        # market.rsi
        # market.macd
        # market.macd_signal
        # market.macd_histogram
        # market.volume

        return market
