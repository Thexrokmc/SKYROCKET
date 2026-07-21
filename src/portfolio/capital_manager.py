class CapitalManager:

    def recommend(

        self,

        available_cash,

        score,

        market_cycle

    ):

        if available_cash <= 0:

            return {

                "amount": 0,

                "percent": 0

            }

        if market_cycle == "BEAR":

            percent = 5

        elif market_cycle == "ACCUMULATION":

            if score >= 90:

                percent = 25

            elif score >= 80:

                percent = 20

            elif score >= 70:

                percent = 15

            else:

                percent = 10

        elif market_cycle == "BULL":

            if score >= 90:

                percent = 15

            elif score >= 80:

                percent = 10

            else:

                percent = 5

        else:

            percent = 5

        amount = (

            available_cash

            * percent

            / 100

        )

        return {

            "amount": round(

                amount,

                2

            ),

            "percent": percent

        }
