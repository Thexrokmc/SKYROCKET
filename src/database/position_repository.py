from datetime import datetime


class PositionRepository:

    def __init__(self, database):

        self.database = database

    def save(

        self,

        position

    ):

        self.database.execute(

            """
            INSERT INTO positions(

                symbol,

                quantity,

                average_price,

                updated_at

            )

            VALUES(

                ?, ?, ?, ?

            )

            ON CONFLICT(symbol)

            DO UPDATE SET

                quantity=excluded.quantity,

                average_price=excluded.average_price,

                updated_at=excluded.updated_at

            """,

            (

                position.symbol,

                position.quantity,

                position.average_price,

                datetime.utcnow().isoformat()

            )

        )

    def get(

        self,

        symbol

    ):

        row = self.database.fetchone(

            """

            SELECT *

            FROM positions

            WHERE symbol=?

            """,

            (

                symbol,

            )

        )

        if row is None:

            return None

        return {

            "symbol": row["symbol"],

            "quantity": row["quantity"],

            "average_price": row["average_price"],

            "updated_at": row["updated_at"]

        }

    def all(self):

        rows = self.database.fetchall(

            """

            SELECT *

            FROM positions

            ORDER BY symbol

            """

        )

        return [

            {

                "symbol": row["symbol"],

                "quantity": row["quantity"],

                "average_price": row["average_price"],

                "updated_at": row["updated_at"]

            }

            for row in rows

        ]

    def delete(

        self,

        symbol

    ):

        self.database.execute(

            """

            DELETE

            FROM positions

            WHERE symbol=?

            """,

            (

                symbol,

            )

        )
