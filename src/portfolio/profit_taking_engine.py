from dataclasses import dataclass
from typing import List


@dataclass
class ProfitTarget:

    level: float
    sell_percent: float


@dataclass
class ProfitAction:

    symbol: str
    action: str
    sell_percent: float
    reason: str


class ProfitTakingEngine:

    def __init__(self):

        self.targets = [

            ProfitTarget(1.25, 10),

            ProfitTarget(1.50, 15),

            ProfitTarget(2.00, 20),

            ProfitTarget(3.00, 25),

            ProfitTarget(5.00, 30)

        ]

    def evaluate(

        self,

        symbol,

        average_price,

        current_price

    ):

        multiple = current_price / average_price

        actions: List[ProfitAction] = []

        for target in self.targets:

            if multiple >= target.level:

                actions.append(

                    ProfitAction(

                        symbol=symbol,

                        action="SELL",

                        sell_percent=target.sell_percent,

                        reason=f"Reached {target.level:.2f}x"

                    )

                )

        return actions
