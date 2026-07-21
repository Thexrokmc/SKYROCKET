class PortfolioManager:

    def __init__(self):

        self.assets = []

    def add_asset(

        self,

        symbol,

        quantity,

        average_price,

        current_price

    ):

        self.assets.append({

            "symbol": symbol,

            "quantity": quantity,

            "average_price": average_price,

            "current_price": current_price

        })

    def total_value(self):

        total = 0.0

        for asset in self.assets:

            total += (

                asset["quantity"]

                * asset["current_price"]

            )

        return total

    def total_cost(self):

        total = 0.0

        for asset in self.assets:

            total += (

                asset["quantity"]

                * asset["average_price"]

            )

        return total

    def total_profit(self):

        return (

            self.total_value()

            - self.total_cost()

        )

    def allocation(self):

        total = self.total_value()

        if total == 0:

            return []

        allocation = []

        for asset in self.assets:

            value = (

                asset["quantity"]

                * asset["current_price"]

            )

            allocation.append({

                "symbol": asset["symbol"],

                "allocation": round(

                    value

                    / total

                    * 100,

                    2

                )

            })

        return allocation
