class PortfolioValidator:

    def validate(

        self,

        portfolio

    ):

        issues = []

        total = portfolio.total_value()

        if total <= 0:

            issues.append(

                "Portfolio is empty."

            )

            return issues

        allocations = portfolio.allocation()

        for asset in allocations:

            allocation = asset["allocation"]

            symbol = asset["symbol"]

            if allocation > 30:

                issues.append(

                    f"{symbol}: Overallocated ({allocation}%)"

                )

            elif allocation < 1:

                issues.append(

                    f"{symbol}: Very small position ({allocation}%)"

                )

        return issues

    def is_valid(

        self,

        portfolio

    ):

        return len(

            self.validate(

                portfolio

            )

        ) == 0
