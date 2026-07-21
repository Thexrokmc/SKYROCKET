class PortfolioSummary:

    def create(

        self,

        portfolio,

        performance

    ):

        summary = {

            "assets": len(portfolio.assets),

            "total_cost": performance["total_cost"],

            "total_value": performance["total_value"],

            "total_profit": performance["total_profit"],

            "total_profit_percent": performance["total_profit_percent"],

            "best_asset": None,

            "worst_asset": None

        }

        if performance["assets"]:

            best = max(

                performance["assets"],

                key=lambda x: x["profit_percent"]

            )

            worst = min(

                performance["assets"],

                key=lambda x: x["profit_percent"]

            )

            summary["best_asset"] = best

            summary["worst_asset"] = worst

        return summary
