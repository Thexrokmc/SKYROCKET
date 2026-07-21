from datetime import datetime


class PortfolioLedger:

    def __init__(self):

        self.transactions = []

    def buy(

        self,

        symbol,

        quantity,

        price,

        timestamp=None

    ):

        self.transactions.append({

            "type": "BUY",

            "symbol": symbol,

            "quantity": quantity,

            "price": price,

            "timestamp": timestamp or datetime.utcnow()

        })

    def sell(

        self,

        symbol,

        quantity,

        price,

        timestamp=None

    ):

        self.transactions.append({

            "type": "SELL",

            "symbol": symbol,

            "quantity": quantity,

            "price": price,

            "timestamp": timestamp or datetime.utcnow()

        })

    def history(

        self,

        symbol=None

    ):

        if symbol is None:

            return self.transactions

        return [

            tx

            for tx in self.transactions

            if tx["symbol"] == symbol

        ]

    def total_transactions(self):

        return len(

            self.transactions

        )

    def clear(self):

        self.transactions.clear()
