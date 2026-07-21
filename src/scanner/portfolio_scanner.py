from scanner.scanner import Scanner


class PortfolioScanner:

    def __init__(self):

        self.scanner = Scanner()

    def analyze(self, symbols):

        portfolio = []

        for symbol in symbols:

            result = self.scanner.analyze(
                symbol
            )

            portfolio.append(
                result
            )

        portfolio.sort(
            key=lambda asset: asset["score"],
            reverse=True
        )

        return portfolio
