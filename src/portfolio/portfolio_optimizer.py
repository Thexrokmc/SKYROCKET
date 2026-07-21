from dataclasses import dataclass
from typing import List


@dataclass
class PortfolioRecommendation:

    symbol: str

    action: str

    target_weight: float

    current_weight: float

    difference: float

    reason: str


class PortfolioOptimizer:

    def __init__(self):

        pass

    def optimize(

        self,

        assets,

        decisions,

        target_weights

    ):

        recommendations: List[PortfolioRecommendation] = []

        for asset in assets:

            symbol = asset.symbol

            decision = decisions[symbol]

            current = asset.weight

            target = target_weights.get(

                symbol,

                current

            )

            action = "HOLD"

            if decision.decision.value in (

                "BUY",

                "STRONG BUY",

                "ACCUMULATE"

            ):

                if current < target:

                    action = "BUY"

            elif decision.decision.value in (

                "SELL",

                "REDUCE"

            ):

                if current > target:

                    action = "SELL"

            recommendations.append(

                PortfolioRecommendation(

                    symbol=symbol,

                    action=action,

                    target_weight=target,

                    current_weight=current,

                    difference=round(

                        target-current,

                        4

                    ),

                    reason=decision.reason

                )

            )

        return recommendations
