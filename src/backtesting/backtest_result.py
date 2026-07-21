class BacktestResult:

    def __init__(

        self

    ):

        self.trades = 0

        self.wins = 0

        self.losses = 0

        self.total_profit = 0.0

        self.win_rate = 0.0

        self.average_profit = 0.0

    def calculate(self):

        if self.trades > 0:

            self.win_rate = round(

                (

                    self.wins

                    / self.trades

                ) * 100,

                2

            )

            self.average_profit = round(

                self.total_profit

                / self.trades,

                2

            )

    def __repr__(self):

        return (

            f"Trades: {self.trades}\n"

            f"Wins: {self.wins}\n"

            f"Losses: {self.losses}\n"

            f"Win Rate: {self.win_rate}%\n"

            f"Total Profit: {self.total_profit}\n"

            f"Average Profit: {self.average_profit}"

        )
