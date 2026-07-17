from portfolio.portfolio_engine import PortfolioEngine


def main():
    print("🚀 SKYROCKET v1.0")
    print("---------------------------")

    portfolio = PortfolioEngine()

    portfolio.load_portfolio()

    portfolio.summary()


if __name__ == "__main__":
    main()
