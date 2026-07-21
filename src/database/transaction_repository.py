class TransactionRepository:

    def __init__(self, database):

        self.database = database

    def save(self, transaction):

        self.database.execute(
            """
            INSERT INTO transactions(
                symbol,
                side,
                quantity,
                price,
                timestamp
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                transaction["symbol"],
                transaction["side"],
                transaction["quantity"],
                transaction["price"],
                transaction["timestamp"]
            )
        )

    def all(self):

        rows = self.database.fetchall(
            """
            SELECT *
            FROM transactions
            ORDER BY timestamp DESC
            """
        )

        return [dict(row) for row in rows]

    def by_symbol(self, symbol):

        rows = self.database.fetchall(
            """
            SELECT *
            FROM transactions
            WHERE symbol=?
            ORDER BY timestamp DESC
            """,
            (symbol,)
        )

        return [dict(row) for row in rows]

    def delete_all(self):

        self.database.execute(
            """
            DELETE FROM transactions
            """
        )

    def count(self):

        row = self.database.fetchone(
            """
            SELECT COUNT(*) AS total
            FROM transactions
            """
        )

        return row["total"]
