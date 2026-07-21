class HealthCheck:

    def __init__(
        self,
        database,
        config,
        logger,
        kraken_client=None
    ):
        self.database = database
        self.config = config
        self.logger = logger
        self.kraken_client = kraken_client

    def run(self):

        results = {}

        # Database
        try:
            self.database.execute("SELECT 1")
            results["database"] = "OK"
        except Exception as e:
            results["database"] = f"ERROR: {e}"

        # Configuration
        try:
            if self.config.base_currency:
                results["configuration"] = "OK"
            else:
                results["configuration"] = "Missing configuration"
        except Exception as e:
            results["configuration"] = f"ERROR: {e}"

        # Kraken API
        if self.kraken_client:
            try:
                self.kraken_client.server_time()
                results["kraken_api"] = "OK"
            except Exception as e:
                results["kraken_api"] = f"ERROR: {e}"
        else:
            results["kraken_api"] = "Not configured"

        return results

    def log_results(self):

        results = self.run()

        for component, status in results.items():

            if status == "OK":

                self.logger.info(
                    f"{component}: {status}"
                )

            else:

                self.logger.warning(
                    f"{component}: {status}"
                )

        return results
