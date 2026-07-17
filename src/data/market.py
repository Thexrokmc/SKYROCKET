class Market:

    def __init__(self):
        self.phase = "UNKNOWN"
        self.btc_trend = "UNKNOWN"
        self.total_market_trend = "UNKNOWN"
        self.fear_greed = None

    def summary(self):
        return {
            "phase": self.phase,
            "btc_trend": self.btc_trend,
            "market_trend": self.total_market_trend,
            "fear_greed": self.fear_greed
        }
