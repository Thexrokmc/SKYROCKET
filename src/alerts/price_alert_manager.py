import json

from pathlib import Path


class PriceAlertManager:

    def __init__(self):

        self.file = Path("price_alerts.json")

        if not self.file.exists():

            self.file.write_text(
                "[]",
                encoding="utf-8"
            )

    def load(self):

        return json.loads(

            self.file.read_text(

                encoding="utf-8"

            )

        )

    def save(self, alerts):

        self.file.write_text(

            json.dumps(

                alerts,

                indent=4

            ),

            encoding="utf-8"

        )

    def add(

        self,

        symbol,

        target_price,

        condition="above"

    ):

        alerts = self.load()

        alerts.append({

            "symbol": symbol,

            "target_price": target_price,

            "condition": condition

        })

        self.save(alerts)

    def check(

        self,

        symbol,

        current_price

    ):

        triggered = []

        alerts = self.load()

        for alert in alerts:

            if alert["symbol"] != symbol:

                continue

            if (

                alert["condition"] == "above"

                and

                current_price >= alert["target_price"]

            ):

                triggered.append(alert)

            elif (

                alert["condition"] == "below"

                and

                current_price <= alert["target_price"]

            ):

                triggered.append(alert)

        return triggered
