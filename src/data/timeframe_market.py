from data.market import MarketData


class TimeframeMarket:

    def __init__(self):

        self.daily = MarketData()

        self.h4 = MarketData()

        self.h1 = MarketData()

        self.m15 = MarketData()
