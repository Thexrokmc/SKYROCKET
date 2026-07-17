class DecisionEngine:

    def decide(self, sky_score):

        score = sky_score["score"]

        if score >= 85:
            action = "STRONG BUY"

        elif score >= 70:
            action = "BUY"

        elif score >= 50:
            action = "HOLD"

        elif score >= 30:
            action = "WATCH"

        else:
            action = "SELL / AVOID"

        return {
            "action": action,
            "score": score,
            "reasons": sky_score["reasons"]
        }
