class Position:

    def __init__(

        self,

        symbol,

        quantity=0.0,

        average_price=0.0

    ):

        self.symbol = symbol

        self.quantity = quantity

        self.average_price = average_price

    def buy(

        self,

        quantity,

        price

    ):

        if quantity <= 0:

            return

        total_cost = (

            self.quantity

            * self.average_price

        ) + (

            quantity

            * price

        )

        self.quantity += quantity

        self.average_price = (

            total_cost

            / self.quantity

        )

    def sell(

        self,

        quantity

    ):

        if quantity <= 0:

            return

        if quantity > self.quantity:

            raise ValueError(

                "Not enough quantity."

            )

        self.quantity -= quantity

        if self.quantity == 0:

            self.average_price = 0.0

    def market_value(

        self,

        current_price

    ):

        return round(

            self.quantity

            * current_price,

            2

        )

    def unrealized_profit(

        self,

        current_price

    ):

        return round(

            (

                current_price

                - self.average_price

            )

            * self.quantity,

            2

        )

    def unrealized_profit_percent(

        self,

        current_price

    ):

        if self.average_price == 0:

            return 0.0

        return round(

            (

                (

                    current_price

                    - self.average_price

                )

                / self.average_price

            )

            * 100,

            2

        )

    def to_dict(self):

        return {

            "symbol": self.symbol,

            "quantity": round(

                self.quantity,

                8

            ),

            "average_price": round(

                self.average_price,

                2

            )

        }
