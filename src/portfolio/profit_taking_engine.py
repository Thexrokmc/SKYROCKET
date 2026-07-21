class ProfitTakingEngine:

    def recommend(

        self,

        score,

        profit_percent

    ):

        if profit_percent < 20:

            return {
                "action": "HOLD",
                "sell_percent": 0
            }

        if score >= 90:

            return {
                "action": "HOLD",
                "sell_percent": 0
            }

        elif score >= 80:

            return {
                "action": "TAKE SMALL PROFIT",
                "sell_percent": 10
            }

        elif score >= 65:

            return {
                "action": "TAKE PROFIT",
                "sell_percent": 20
            }

        elif score >= 50:

            return {
                "action": "REDUCE POSITION",
                "sell_percent": 35
            }

        else:

            return {
                "action": "EXIT",
                "sell_percent": 50
            }
