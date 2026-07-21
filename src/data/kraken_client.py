import requests


class KrakenClient:

    BASE_URL = "https://futures.kraken.com/api/charts/v1/trade"

    def get_candles(
        self,
        symbol: str,
        interval: str = "1h"
    ):

        params = {
            "symbol": symbol,
            "interval": interval
        }

        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()
