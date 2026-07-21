from data.kraken_client import KrakenClient
from data.timeframe_market import TimeframeMarket


class KrakenMarketProvider:

    def __init__(

        self,

        client=None

    ):

        self.client = client or KrakenClient()

    def get(

        self,

        pair

    ):

        ticker = self.client.ticker(

            pair

        )

        pair_name = next(

            iter(

                ticker

            )

        )

        data = ticker[

            pair_name

        ]

        price = float(

            data["c"][0]

        )

        bid = float(

            data["b"][0]

        )

        ask = float(

            data["a"][0]

        )

        volume = float(

            data["v"][1]

        )

        return TimeframeMarket(

            symbol=pair,

            price=price,
            bid=bid,
            ask=ask,
            volume=volume
        )
