class PortfolioEngine:
    def __init__(self):
        self.assets = []

    def load_portfolio(self):
        print("📂 Portfolio loaded.")

    def summary(self):
        print(f"Assets in portfolio: {len(self.assets)}")
