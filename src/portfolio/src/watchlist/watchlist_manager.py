import json

from pathlib import Path


class WatchlistManager:

    def __init__(self):

        self.file = Path("watchlist.json")

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

    def save(self, watchlist):

        self.file.write_text(

            json.dumps(

                watchlist,

                indent=4

            ),

            encoding="utf-8"

        )

    def add(self, symbol):

        watchlist = self.load()

        if symbol not in watchlist:

            watchlist.append(symbol)

            self.save(watchlist)

    def remove(self, symbol):

        watchlist = self.load()

        if symbol in watchlist:

            watchlist.remove(symbol)

            self.save(watchlist)

    def contains(self, symbol):

        return symbol in self.load()
