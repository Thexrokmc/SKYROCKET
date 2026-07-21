import requests


class KrakenClient:

    BASE_URL = "https://api.kraken.com"

    def __init__(

        self,

        timeout=10

    ):

        self.timeout = timeout

    def _get(

        self,

        endpoint,

        params=None

    ):

        url = f"{self.BASE_URL}{endpoint}"

        response = requests.get(

            url,

            params=params,

            timeout=self.timeout

        )

        response.raise_for_status()

        data = response.json()

        if data.get("error"):

            raise Exception(

                ", ".join(data["error"])

            )

        return data["result"]

    def server_time(self):

        return self._get(

            "/0/public/Time"

        )

    def ticker(

        self,

        pair

    ):

        return self._get(

            "/0/public/Ticker",

            {

                "pair": pair

            }

        )

    def ohlc(

        self,

        pair,

        interval=60

    ):

        return self._get(

            "/0/public/OHLC",

            {

                "pair": pair,

                "interval": interval

            }

        )
