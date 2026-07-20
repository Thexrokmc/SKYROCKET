class MarketData:

    def __init__(self):
        self.symbol = ""
        self.price = None
        self.volume = None

        self.ema50 = None
        self.ema200 = None

        self.rsi = None

        self.macd = None
        self.macd_signal = None
        self.macd_histogram = None
