from core.config import Config
from core.logger import get_logger
from core.health_check import HealthCheck
from core.version import VersionManager


def main():

    logger = get_logger("SKYROCKET")

    logger.info("=" * 60)
    logger.info("Starting SKYROCKET")
    logger.info("Version: %s", VersionManager.full_version())
    logger.info("=" * 60)

    config = Config()

    health = HealthCheck(
        database=None,
        config=config,
        logger=logger,
        kraken_client=None
    )

    results = health.log_results()

    logger.info("Health Check Complete")

    if any(
        value not in ("OK", "Not configured")
        for value in results.values()
    ):
        logger.error("Startup aborted due to failed health checks.")
        return

    logger.info("Application initialized successfully.")

    #
    # Future pipeline
    #
    # 1. Connect Kraken
    # 2. Sync Portfolio
    # 3. Download Market Data
    # 4. Calculate Indicators
    # 5. Build Facts
    # 6. Execute Rules
    # 7. Calculate SKY Score
    # 8. Generate Decisions
    # 9. Portfolio Rebalancing
    # 10. Reports

    logger.info("SKYROCKET finished successfully.")


if __name__ == "__main__":
    main()
