import sqlite3
from pathlib import Path


class Database:

    def __init__(self, db_path="skyrocket.db"):

        self.db_path = Path(db_path)
        self.connection = sqlite3.connect(
            self.db_path
        )

        self.connection.row_factory = sqlite3.Row

    def execute(

        self,

        query,

        parameters=()

    ):

        cursor = self.connection.cursor()

        cursor.execute(

            query,

            parameters

        )

        self.connection.commit()

        return cursor

    def fetchone(

        self,

        query,

        parameters=()

    ):

        cursor = self.execute(

            query,

            parameters

        )

        return cursor.fetchone()

    def fetchall(

        self,

        query,

        parameters=()

    ):

        cursor = self.execute(

            query,

            parameters

        )

        return cursor.fetchall()

    def close(self):

        self.connection.close()
