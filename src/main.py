from database.database import Database
from database.database_manager import DatabaseManager


def main():

    print("=" * 50)
    print("SKYROCKET")
    print("Starting...")
    print("=" * 50)

    db = Database()

    DatabaseManager(
        db
    ).initialize()

    print("✓ Database initialized")

    print("System ready.")

    db.close()


if __name__ == "__main__":
    main()
