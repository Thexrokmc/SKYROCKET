import base64
import hashlib
import hmac
import time
import urllib.parse

import requests


class KrakenAccountClient:

    BASE_URL = "https://api.kraken.com"

    def __init__(

        self,

        api_key,

        api_secret,

        timeout=15

    ):

        self.api_key = api_key
        self.api_secret = api_secret
        self.timeout = timeout

    def _sign(

        self,

        urlpath,

        data

    ):

        postdata = urllib.parse.urlencode(data)

        encoded = (

            str(data["nonce"])

            + postdata

        ).encode()

        message = (

            urlpath.encode()

            + hashlib.sha256(

                encoded

            ).digest()

        )

        signature = hmac.new(

            base64.b64decode(

                self.api_secret

            ),

            message,

            hashlib.sha512

        )

        return base64.b64encode(

            signature.digest()

        ).decode()

    def _private(

        self,

        endpoint,

        data=None

    ):

        data = data or {}

        data["nonce"] = str(

            int(

                time.time()

                * 1000

            )

        )

        headers = {

            "API-Key": self.api_key,

            "API-Sign": self._sign(

                endpoint,

                data

            )

        }

        response = requests.post(

            self.BASE_URL + endpoint,

            headers=headers,

            data=data,

            timeout=self.timeout

        )

        response.raise_for_status()

        payload = response.json()

        if payload["error"]:

            raise Exception(

                ", ".join(

                    payload["error"]

                )

            )

        return payload["result"]

    def balances(self):

        return self._private(

            "/0/private/Balance"

        )

    def trade_balance(self):

        return self._private(

            "/0/private/TradeBalance"
        )
