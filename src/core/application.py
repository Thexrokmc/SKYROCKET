from core.bootstrap import Bootstrap


class Application:
    """
    Main application lifecycle.
    """

    def __init__(self):
        self.bootstrap = Bootstrap()
        self.services = {}

    def start(self):

        self.bootstrap.initialize()

        self.bootstrap.run_health_check()

        self.services = self.bootstrap.services()

        logger = self.services["logger"]

        logger.info("Application started.")

    def run(self):

        logger = self.services["logger"]

        logger.info("Running analysis pipeline...")

        #
        # Future pipeline
        #
        # Portfolio Sync
        # Market Data
        # Indicators
        # Facts
        # Rules
        # SKY Score
        # Decision Engine
        # Reports
        #

        logger.info("Pipeline completed.")

    def stop(self):

        logger = self.services["logger"]

        logger.info("Shutting down application.")

    def execute(self):

        self.start()

        try:

            self.run()

        finally:

            self.stop()
