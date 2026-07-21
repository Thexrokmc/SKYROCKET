class ReportGenerator:

    def generate(

        self,

        symbol,

        market_cycle,

        score,

        decision,

        reasons

    ):

        report = []

        report.append("=" * 50)

        report.append(f"Asset: {symbol}")

        report.append(f"Market Cycle: {market_cycle}")

        report.append(f"SkyScore: {score}")

        report.append(f"Decision: {decision}")

        report.append("")

        report.append("Reasons:")

        for reason in reasons:

            report.append(
                f"- {reason}"
            )

        report.append("=" * 50)

        return "\n".join(report)
