from database.database import Database


class DatabaseManager:

    def __init__(self, database: Database):

        self.database = database

    def initialize(self):

        self.create_settings_table()
        self.create_positions_table()
        self.create_transactions_table()
        self.create_reports_table()

    def create_settings_table(self):

        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS settings(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE,
                value TEXT
            )
            """
        )

    def create_positions_table(self):

        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS positions(
                symbol TEXT PRIMARY KEY,
                quantity REAL,
                average_price REAL,
                updated_at TEXT
            )
            """
        )

    def create_transactions_table(self):

        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                side TEXT,
                quantity REAL,
                price REAL,
                timestamp TEXT
            )
            """
        )

    def create_reports_table(self):

        self.database.execute(
            """
            CREATE TABLE IF NOT EXISTS reports(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                score REAL,
                decision TEXT,
                report TEXT,
                created_at TEXT
            )
            """
        )
