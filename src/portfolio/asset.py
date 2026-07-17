class Asset:
    def __init__(
        self,
        symbol,
        quantity,
        average_cost,
        current_price=0.0
    ):
        self.symbol = symbol
        self.quantity = quantity
        self.average_cost = average_cost
        self.current_price = current_price

    @property
    def value(self):
        return self.quantity * self.current_price

    @property
    def cost(self):
        return self.quantity * self.average_cost

    @property
    def pnl(self):
        return self.value - self.cost
