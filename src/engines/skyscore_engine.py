class SkyScoreEngine:

    def calculate(self, rule_results):

        total_score = 0
        reasons = []

        for result in rule_results:

            total_score += result["score"]
            reasons.append(result["reason"])

        return {
            "score": total_score,
            "reasons": reasons
        }
