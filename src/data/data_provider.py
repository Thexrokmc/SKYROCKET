from data.market import MarketData


class DataProvider:

    def load_market_data(self) -> MarketData:

        market = MarketData()

        market.symbol = "BTCUSDT"

        market.price = 118000

        market.ema50 = 115000

        market.ema200 = 108000

        market.rsi = 42

        market.macd = 125

        market.macd_signal = 118

        market.macd_histogram = 7

        market.volume = 1250000000

        return market
