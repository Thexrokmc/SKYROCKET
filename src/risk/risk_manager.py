class RiskManager:

    def __init__(self):

        self.max_risk_per_trade = 2.0

        self.max_portfolio_risk = 10.0

    def calculate_position_size(

        self,

        account_balance,

        entry,

        stop_loss

    ):

        risk_amount = (

            account_balance

            * self.max_risk_per_trade

            / 100

        )

        distance = abs(

            entry - stop_loss

        )

        if distance == 0:

            return 0

        position_size = (

            risk_amount

            / distance

        )

        return round(

            position_size,

            4

        )
