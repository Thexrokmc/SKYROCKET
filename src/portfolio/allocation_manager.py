class AllocationManager:

    def __init__(self):

        self.max_asset_allocation = 20.0

    def recommend(

        self,

        portfolio_value,

        asset_value

    ):

        if portfolio_value == 0:

            return "BUY"

        allocation = (

            asset_value

            / portfolio_value

        ) * 100

        if allocation < 5:

            return "STRONG BUY"

        elif allocation < 10:

            return "BUY"

        elif allocation < self.max_asset_allocation:

            return "ACCUMULATE"

        else:

            return "FULL"
