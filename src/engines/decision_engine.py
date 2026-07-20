from engines.decision import Decision
from rules.rule_result import RuleResult


class DecisionEngine:

    def decide(self, results: list[RuleResult]) -> Decision:
        buy_score = 0
        sell_score = 0
        reasons = []

        for result in results:
            if result.passed:
                buy_score += result.weight
                reasons.append(result.name)

        confidence = min(buy_score, 100)

        if buy_score >= 70:
            action = "BUY"
        elif buy_score >= 40:
            action = "HOLD"
        else:
            action = "SELL"

        return Decision(
            action=action,
            buy_score=buy_score,
            sell_score=sell_score,
            confidence=confidence,
            reasons=reasons
        )
