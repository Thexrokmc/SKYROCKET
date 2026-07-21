class PerformanceManager:

    def asset_performance(

        self,

        quantity,

        average_price,

        current_price

    ):

        cost = quantity * average_price

        value = quantity * current_price

        profit = value - cost

        if cost == 0:

            profit_percent = 0.0

        else:

            profit_percent = (

                profit

                / cost

            ) * 100

        return {

            "cost": round(

                cost,

                2

            ),

            "value": round(

                value,

                2

            ),

            "profit": round(

                profit,

                2

            ),

            "profit_percent": round(

                profit_percent,

                2

            )

        }

    def portfolio_performance(

        self,

        portfolio

    ):

        total_cost = 0.0

        total_value = 0.0

        assets = []

        for asset in portfolio.assets:

            result = self.asset_performance(

                asset["quantity"],

                asset["average_price"],

                asset["current_price"]

            )

            assets.append({

                "symbol": asset["symbol"],

                **result

            })

            total_cost += result["cost"]

            total_value += result["value"]

        total_profit = (

            total_value

            - total_cost

        )

        if total_cost == 0:

            total_profit_percent = 0.0

        else:

            total_profit_percent = (

                total_profit

                / total_cost

            ) * 100

        return {

            "assets": assets,

            "total_cost": round(

                total_cost,

                2

            ),

            "total_value": round(

                total_value,

                2

            ),

            "total_profit": round(

                total_profit,

                2

            ),

            "total_profit_percent": round(

                total_profit_percent,

                2

            )

        }
