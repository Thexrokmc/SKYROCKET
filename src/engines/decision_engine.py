from decision.decision import Decision
from decision.sky_score_engine import SkyScoreEngine


class DecisionEngine:

    def __init__(self):

        self.sky_score = SkyScoreEngine()

    def decide(self, results):

        decision = Decision()

        score = self.sky_score.calculate(results)

        decision.score = score

        for result in results:

            if result.passed:

                decision.add_reason(
                    result.name
                )

        if score >= 80:

            decision.action = "BUY"

        elif score >= 60:

            decision.action = "ACCUMULATE"

        elif score >= 40:

            decision.action = "HOLD"

        else:

            decision.action = "WAIT"

        return decision
