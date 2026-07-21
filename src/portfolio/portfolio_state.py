from portfolio.portfolio_manager import PortfolioManager
from portfolio.portfolio_ledger import PortfolioLedger
from portfolio.performance_manager import PerformanceManager
from portfolio.portfolio_summary import PortfolioSummary


class PortfolioState:

    def __init__(self):

        self.portfolio = PortfolioManager()

        self.ledger = PortfolioLedger()

        self.performance = PerformanceManager()

        self.summary = PortfolioSummary()

    def report(self):

        performance = self.performance.portfolio_performance(

            self.portfolio

        )

        return self.summary.create(

            self.portfolio,

            performance

        )

    def total_value(self):

        return self.portfolio.total_value()

    def total_profit(self):

        return self.performance.portfolio_performance(

            self.portfolio

        )["total_profit"]

    def allocation(self):

        return self.portfolio.allocation()

    def history(self):

        return self.ledger.history()
