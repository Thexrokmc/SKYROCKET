class RiskEngine:

    def recommend(

        self,

        portfolio_value,

        asset_value,

        score,

        market_cycle

    ):

        if portfolio_value <= 0:

            return {

                "risk": "LOW",

                "max_buy": 0.0

            }

        allocation = (

            asset_value

            / portfolio_value

        ) * 100

        if market_cycle == "BEAR":

            max_allocation = 10

        elif market_cycle == "ACCUMULATION":

            max_allocation = 20

        else:

            max_allocation = 25

        remaining = max(

            0,

            max_allocation

            - allocation

        )

        max_buy = (

            portfolio_value

            * remaining

            / 100

        )

        if score >= 90:

            risk = "HIGH"

        elif score >= 75:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        return {

            "risk": risk,

            "current_allocation": round(

                allocation,

                2

            ),

            "max_allocation": max_allocation,

            "remaining_allocation": round(

                remaining,

                2

            ),

            "max_buy": round(

                max_buy,

                2

            )

        }
