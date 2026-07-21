class Portfolio:

    def __init__(self):

        self.assets = []

    def add(self, asset):

        self.assets.append(asset)

    def total_value(self):

        total = 0

        for asset in self.assets:
            total += asset.market_value

        return total
