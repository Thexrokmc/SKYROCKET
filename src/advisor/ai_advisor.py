class AIAdvisor:

    def advise(

        self,

        market_cycle,

        score,

        dca_action,

        profit_action,

        rebalance_action

    ):

        recommendation = []

        recommendation.append(
            f"Market Cycle: {market_cycle}"
        )

        recommendation.append(
            f"SkyScore: {score}"
        )

        recommendation.append(
            f"DCA: {dca_action}"
        )

        recommendation.append(
            f"Profit Taking: {profit_action}"
        )

        recommendation.append(
            f"Rebalancing: {rebalance_action}"
        )

        if market_cycle == "BULL" and score >= 80:

            recommendation.append(
                "Overall: BUY"
            )

        elif market_cycle == "ACCUMULATION":

            recommendation.append(
                "Overall: ACCUMULATE"
            )

        elif market_cycle == "BEAR":

            recommendation.append(
                "Overall: DEFENSIVE"
            )

        else:

            recommendation.append(
                "Overall: HOLD"
            )

        return recommendation
