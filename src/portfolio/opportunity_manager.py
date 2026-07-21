class OpportunityManager:

    def find(

        self,

        portfolio,

        analyses

    ):

        opportunities = []

        for analysis in analyses:

            if (

                analysis.score >= 80

                and

                analysis.market_cycle

                in [

                    "BULL",

                    "ACCUMULATION"

                ]

            ):

                allocation = 0

                for asset in portfolio.assets:

                    if (

                        asset["symbol"]

                        == analysis.symbol

                    ):

                        total = portfolio.total_value()

                        if total > 0:

                            allocation = (

                                asset["quantity"]

                                * asset["current_price"]

                                / total

                            ) * 100

                        break

                opportunities.append({

                    "symbol": analysis.symbol,

                    "score": analysis.score,

                    "market_cycle": analysis.market_cycle,

                    "decision": analysis.decision,

                    "allocation": round(

                        allocation,

                        2

                    )

                })

        opportunities.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        return opportunities
