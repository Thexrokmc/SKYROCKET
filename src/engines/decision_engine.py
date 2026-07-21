from decision.sky_score_engine import SkyScoreEngine


class DecisionEngine:

    def __init__(self):

        self.sky_score = SkyScoreEngine()

    def decide(self, results):

        score = self.sky_score.calculate(results)

        if score >= 80:
            action = "BUY"

        elif score >= 60:
            action = "ACCUMULATE"

        elif score >= 40:
            action = "HOLD"

        else:
            action = "WAIT"

        return {
            "action": action,
            "score": score
        }
