from dataclasses import dataclass
from typing import List


@dataclass
class RebalanceAction:

    symbol: str

    action: str

    amount_eur: float

    reason: str


class RebalancingEngine:

    def __init__(

        self,

        minimum_trade=20.0

    ):

        self.minimum_trade = minimum_trade

    def build_plan(

        self,

        portfolio_value,

        recommendations

    ):

        plan: List[RebalanceAction] = []

        for recommendation in recommendations:

            difference = recommendation.difference

            amount = abs(

                difference

            ) * portfolio_value

            if amount < self.minimum_trade:

                continue

            if recommendation.action == "BUY":

                action = "BUY"

            elif recommendation.action == "SELL":

                action = "SELL"

            else:

                continue

            plan.append(

                RebalanceAction(

                    symbol=recommendation.symbol,

                    action=action,

                    amount_eur=round(

                        amount,

                        2

                    ),

                    reason=recommendation.reason

                )

            )

        return sorted(

            plan,

            key=lambda x: x.amount_eur,

            reverse=True

        )
