from core.config import Config
from core.logger import get_logger
from core.health_check import HealthCheck
from core.version import VersionManager


class Bootstrap:

    def __init__(self):

        self.config = None
        self.logger = None
        self.health_check = None

    def initialize(self):

        self.logger = get_logger("SKYROCKET")

        self.logger.info(
            "Initializing SKYROCKET %s",
            VersionManager.full_version()
        )

        self.config = Config()

        self.health_check = HealthCheck(
            database=None,
            config=self.config,
            logger=self.logger,
            kraken_client=None
        )

        return self

    def run_health_check(self):

        return self.health_check.log_results()

    def services(self):

        return {
            "config": self.config,
            "logger": self.logger,
            "health_check": self.health_check
        }
