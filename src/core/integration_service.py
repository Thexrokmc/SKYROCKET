from datetime import datetime


class IntegrationService:

    def __init__(

        self,

        portfolio_sync,

        engine,

        report_repository

    ):

        self.portfolio_sync = portfolio_sync
        self.engine = engine
        self.report_repository = report_repository

    def run(

        self,

        symbols,

        portfolio_value,

        asset_values,

        available_cash,

        fear_greed,

        days_since_last_buy

    ):

        self.portfolio_sync.sync()

        reports = []

        for symbol in symbols:

            report = self.engine.analyze(

                symbol=symbol,

                portfolio_value=portfolio_value,

                asset_value=asset_values.get(

                    symbol,

                    0

                ),

                available_cash=available_cash,

                fear_greed=fear_greed,

                days_since_last_buy=days_since_last_buy

            )

            self.report_repository.save(

                symbol=symbol,

                score=report["score"],

                decision=report["decision"],

                report=report,

                created_at=datetime.utcnow().isoformat()

            )

            reports.append(

                report

            )

        return reports
