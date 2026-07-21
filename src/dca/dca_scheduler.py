class DCAScheduler:

    def recommend(

        self,

        score,

        market_cycle,

        fear_greed,

        days_since_last_buy

    ):

        if days_since_last_buy < 7:

            return {

                "buy": False,

                "reason": "Recent purchase."

            }

        if market_cycle == "BEAR":

            return {

                "buy": True,

                "reason": "Bear market accumulation."

            }

        if market_cycle == "ACCUMULATION":

            if score >= 80:

                return {

                    "buy": True,

                    "reason": "High SkyScore."

                }

        if fear_greed < 30:

            return {

                "buy": True,

                "reason": "Extreme fear."

            }

        return {

            "buy": False,

            "reason": "Wait."

        }
