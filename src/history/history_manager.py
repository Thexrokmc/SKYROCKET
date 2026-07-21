import json
from pathlib import Path


class HistoryManager:

    def __init__(self):

        self.file = Path("history.json")

        if not self.file.exists():

            self.file.write_text(
                "[]",
                encoding="utf-8"
            )

    def save(self, result):

        history = json.loads(

            self.file.read_text(
                encoding="utf-8"
            )

        )

        history.append({

            "symbol": result.symbol,

            "price": result.price,

            "score": result.score,

            "market_cycle": result.market_cycle,

            "decision": result.decision,

            "reasons": result.reasons

        })

        self.file.write_text(

            json.dumps(

                history,

                indent=4

            ),

            encoding="utf-8"

        )

    def load(self):

        return json.loads(

            self.file.read_text(

                encoding="utf-8"

            )

        )
