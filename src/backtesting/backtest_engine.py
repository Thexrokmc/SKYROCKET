from backtesting.backtest_result import BacktestResult


class BacktestEngine:

    def __init__(self):

        self.result = BacktestResult()

    def run(

        self,

        trades

    ):

        for trade in trades:

            self.result.trades += 1

            profit = trade["profit"]

            self.result.total_profit += profit

            if profit > 0:

                self.result.wins += 1

            else:

                self.result.losses += 1

        self.result.calculate()

        return self.result

    def reset(self):

        self.result = BacktestResult()
