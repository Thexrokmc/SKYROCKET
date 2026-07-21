from core.skyrocket_engine import SkyrocketEngine


class SkyrocketApp:

    def __init__(

        self,

        engine: SkyrocketEngine

    ):

        self.engine = engine

    def run(

        self,

        symbols,

        portfolio_value,

        asset_values,

        available_cash,

        fear_greed,

        days_since_last_buy

    ):

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

            reports.append(

                report

            )

        return reports
