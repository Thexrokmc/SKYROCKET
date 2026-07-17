from .asset import Asset


class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset: Asset):
        self.assets.append(asset)

    @property
    def total_value(self):
        return sum(asset.value for asset in self.assets)

    @property
    def total_cost(self):
        return sum(asset.cost for asset in self.assets)

    @property
    def total_pnl(self):
        return self.total_value - self.total_cost
