import os
from pathlib import Path

from dotenv import load_dotenv


class ConfigLoader:

    def __init__(self, env_file=".env"):

        env_path = Path(env_file)

        if env_path.exists():

            load_dotenv(env_path)

    def get(self, key, default=None):

        return os.getenv(key, default)

    @property
    def kraken_api_key(self):

        return self.get("KRAKEN_API_KEY")

    @property
    def kraken_api_secret(self):

        return self.get("KRAKEN_API_SECRET")

    @property
    def database_path(self):

        return self.get(

            "DATABASE_PATH",

            "skyrocket.db"

        )

    @property
    def base_currency(self):

        return self.get(

            "BASE_CURRENCY",

            "EUR"

        )

    @property
    def log_level(self):

        return self.get(

            "LOG_LEVEL",

            "INFO"

        )
