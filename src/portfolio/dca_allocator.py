from dataclasses import dataclass
from typing import List


@dataclass
class DCAAllocation:

    symbol: str

    amount_eur: float

    percentage: float

    reason: str


class DCAAllocator:

    def allocate(

        self,

        monthly_budget: float,

        recommendations

    ):

        buy_assets = [

            r for r in recommendations

            if r.action == "BUY"

        ]

        if not buy_assets:

            return []

        total_gap = sum(

            max(r.difference, 0)

            for r in buy_assets

        )

        allocations: List[DCAAllocation] = []

        for asset in buy_assets:

            weight = (

                asset.difference / total_gap

                if total_gap > 0

                else 1 / len(buy_assets)

            )

            amount = round(

                monthly_budget * weight,

                2

            )

            allocations.append(

                DCAAllocation(

                    symbol=asset.symbol,

                    amount_eur=amount,

                    percentage=round(

                        weight * 100,

                        2

                    ),

                    reason=asset.reason

                )

            )

        return sorted(

            allocations,

            key=lambda x: x.amount_eur,

            reverse=True

        )
