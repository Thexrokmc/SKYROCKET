class Trade:

    def __init__(

        self,

        symbol,

        entry_price,

        exit_price,

        quantity

    ):

        self.symbol = symbol

        self.entry_price = entry_price

        self.exit_price = exit_price

        self.quantity = quantity

    @property
    def cost(self):

        return (

            self.entry_price

            * self.quantity

        )

    @property
    def value(self):

        return (

            self.exit_price

            * self.quantity

        )

    @property
    def profit(self):

        return (

            self.value

            - self.cost

        )

    @property
    def profit_percent(self):

        if self.cost == 0:

            return 0.0

        return round(

            (

                self.profit

                / self.cost

            ) * 100,

            2

        )

    @property
    def is_win(self):

        return self.profit > 0

    def to_dict(self):

        return {

            "symbol": self.symbol,

            "entry_price": self.entry_price,

            "exit_price": self.exit_price,

            "quantity": self.quantity,

            "cost": round(self.cost, 2),

            "value": round(self.value, 2),

            "profit": round(self.profit, 2),

            "profit_percent": self.profit_percent,

            "is_win": self.is_win

        }

    def __repr__(self):

        return (

            f"Trade("

            f"{self.symbol}, "

            f"{self.profit_percent}%"

            f")"

        )
