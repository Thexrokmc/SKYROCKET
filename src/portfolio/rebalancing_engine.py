class RebalancingEngine:

    def rebalance(self, portfolio):

        recommendations = []

        total_value = sum(
            asset.market_value
            for asset in portfolio.assets
        )

        if total_value == 0:
            return recommendations

        for asset in portfolio.assets:

            allocation = (
                asset.market_value
                / total_value
            ) * 100

            if allocation > 20:

                recommendations.append({

                    "symbol": asset.symbol,

                    "action": "REDUCE",

                    "allocation": round(
                        allocation,
                        2
                    )

                })

            elif allocation < 5:

                recommendations.append({

                    "symbol": asset.symbol,

                    "action": "INCREASE",

                    "allocation": round(
                        allocation,
                        2
                    )

                })

            else:

                recommendations.append({

                    "symbol": asset.symbol,

                    "action": "KEEP",

                    "allocation": round(
                        allocation,
                        2
                    )

                })

        return recommendations
