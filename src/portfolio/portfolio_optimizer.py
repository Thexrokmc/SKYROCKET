class PortfolioOptimizer:

    def optimize(self, portfolio):

        buy = []

        accumulate = []

        hold = []

        wait = []

        for asset in portfolio:

            score = asset["score"]

            if score >= 80:

                buy.append(asset)

            elif score >= 60:

                accumulate.append(asset)

            elif score >= 40:

                hold.append(asset)

            else:

                wait.append(asset)

        return {

            "buy": buy,

            "accumulate": accumulate,

            "hold": hold,

            "wait": wait

        }
