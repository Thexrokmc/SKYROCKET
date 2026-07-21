class PortfolioSyncService:

    def __init__(

        self,

        account_client,

        portfolio_manager

    ):

        self.account_client = account_client
        self.portfolio_manager = portfolio_manager

    def sync(self):

        balances = self.account_client.balances()

        self.portfolio_manager.clear()

        for symbol, balance in balances.items():

            quantity = float(balance)

            if quantity <= 0:

                continue

            self.portfolio_manager.add_position(

                symbol=symbol,

                quantity=quantity

            )

        return self.portfolio_manager
