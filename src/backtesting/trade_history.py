from backtesting.trade import Trade


class TradeHistory:

    def __init__(self):

        self.trades = []

    def add_trade(

        self,

        trade: Trade

    ):

        self.trades.append(trade)

    def total_profit(self):

        return round(

            sum(

                trade.profit

                for trade in self.trades

            ),

            2

        )

    def total_cost(self):

        return round(

            sum(

                trade.cost

                for trade in self.trades

            ),

            2

        )

    def win_rate(self):

        if not self.trades:

            return 0.0

        wins = sum(

            1

            for trade in self.trades

            if trade.is_win

        )

        return round(

            wins

            / len(self.trades)

            * 100,

            2

        )

    def best_trade(self):

        if not self.trades:

            return None

        return max(

            self.trades,

            key=lambda trade: trade.profit

        )

    def worst_trade(self):

        if not self.trades:

            return None

        return min(

            self.trades,

            key=lambda trade: trade.profit

        )

    def summary(self):

        return {

            "trades": len(self.trades),

            "total_cost": self.total_cost(),

            "total_profit": self.total_profit(),

            "win_rate": self.win_rate(),

            "best_trade": self.best_trade(),

            "worst_trade": self.worst_trade()

        }
