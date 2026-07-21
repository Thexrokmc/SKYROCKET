from portfolio.portfolio import Portfolio


class PortfolioAnalyzer:

    def analyze(self, portfolio: Portfolio):

        for asset in portfolio.assets:

            if asset.score >= 80:

                asset.action = "BUY"

            elif asset.score >= 60:

                asset.action = "ACCUMULATE"

            elif asset.score >= 40:

                asset.action = "HOLD"

            else:

                asset.action = "WAIT"

        return portfolio
