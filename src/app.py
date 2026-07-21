from scanner.portfolio_scanner import PortfolioScanner

from portfolio.portfolio_optimizer import (
    PortfolioOptimizer
)

from portfolio.dca_manager import (
    DCAManager
)

from portfolio.profit_taking_engine import (
    ProfitTakingEngine
)

from portfolio.rebalancing_engine import (
    RebalancingEngine
)


def main():

    symbols = [

        "PF_XBTUSD",
        "PF_ETHUSD",
        "PF_XRPUSD",
        "PF_SOLUSD",
        "PF_LINKUSD",
        "PF_SUIUSD"

    ]

    scanner = PortfolioScanner()

    portfolio = scanner.analyze(
        symbols
    )

    optimizer = PortfolioOptimizer()

    optimized = optimizer.optimize(
        portfolio
    )

    print()

    print("=" * 60)

    print("SKYROCKET")

    print("=" * 60)

    print()

    for group in optimized:

        print(group.upper())

        print("-" * 30)

        for asset in optimized[group]:

            print(

                asset["symbol"],

                "Score:",

                asset["score"]

            )

        print()


if __name__ == "__main__":

    main()
