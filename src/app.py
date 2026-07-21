from config.symbols import Symbols

from scanner.portfolio_scanner import PortfolioScanner

from portfolio.portfolio_optimizer import PortfolioOptimizer

from portfolio.dca_manager import DCAManager

from portfolio.profit_taking_engine import ProfitTakingEngine

from portfolio.rebalancing_engine import RebalancingEngine


def main():

    symbols = Symbols.all()

    scanner = PortfolioScanner()

    portfolio = scanner.analyze(
        symbols
    )

    optimizer = PortfolioOptimizer()

    optimized = optimizer.optimize(
        portfolio
    )

    dca_manager = DCAManager()

    profit_engine = ProfitTakingEngine()

    rebalance_engine = RebalancingEngine()

    print()

    print("=" * 60)

    print("🚀 SKYROCKET")

    print("=" * 60)

    print()

    for group in optimized:

        print(group.upper())

        print("-" * 30)

        for asset in optimized[group]:

            print(
                f"{asset['symbol']} | Score: {asset['score']}"
            )

        print()

    print("=" * 60)

    print("PORTFOLIO TOOLS")

    print("=" * 60)

    print()

    print("DCA Recommendation")

    print(
        dca_manager.recommend(
            85,
            8
        )
    )

    print()

    print("Profit Taking")

    print(
        profit_engine.recommend(
            82,
            35
        )
    )

    print()

    print("Rebalancing")

    print(
        rebalance_engine.rebalance(
            portfolio
        )
    )

    print()

    print("=" * 60)

    print("END OF REPORT")

    print("=" * 60)


if __name__ == "__main__":

    main()
