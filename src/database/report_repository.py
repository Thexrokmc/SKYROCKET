import json


class ReportRepository:

    def __init__(self, database):

        self.database = database

    def save(

        self,

        symbol,

        score,

        decision,

        report,

        created_at

    ):

        self.database.execute(

            """
            INSERT INTO reports(

                symbol,

                score,

                decision,

                report,

                created_at

            )

            VALUES(

                ?, ?, ?, ?, ?

            )
            """,

            (

                symbol,

                score,

                decision,

                json.dumps(report),

                created_at

            )

        )

    def latest(

        self,

        symbol

    ):

        row = self.database.fetchone(

            """

            SELECT *

            FROM reports

            WHERE symbol=?

            ORDER BY created_at DESC

            LIMIT 1

            """,

            (

                symbol,

            )

        )

        if row is None:

            return None

        result = dict(row)

        result["report"] = json.loads(

            result["report"]

        )

        return result

    def history(

        self,

        symbol

    ):

        rows = self.database.fetchall(

            """

            SELECT *

            FROM reports

            WHERE symbol=?

            ORDER BY created_at DESC

            """,

            (

                symbol,

            )

        )

        results = []

        for row in rows:

            item = dict(row)

            item["report"] = json.loads(

                item["report"]

            )

            results.append(item)

        return results

    def delete_all(self):

        self.database.execute(

            """

            DELETE FROM reports

            """

        )
