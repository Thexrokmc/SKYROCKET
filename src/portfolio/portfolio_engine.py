import json

from portfolio.portfolio import Portfolio
from portfolio.asset import Asset


class PortfolioEngine:

    def load_portfolio(self):

        portfolio = Portfolio()

        with open("config/portfolio.json", "r") as file:

            data = json.load(file)

        for item in data.get("assets", []):

            asset = Asset(
                symbol=item["symbol"],
                quantity=item["quantity"],
                average_cost=item["average_cost"],
                current_price=item.get("current_price", 0)
            )

            portfolio.add_asset(asset)

        return portfolio
