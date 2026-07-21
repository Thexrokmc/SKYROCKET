from dataclasses import dataclass
from enum import Enum


class Decision(Enum):

    STRONG_BUY = "STRONG BUY"
    BUY = "BUY"
    ACCUMULATE = "ACCUMULATE"
    HOLD = "HOLD"
    REDUCE = "REDUCE"
    SELL = "SELL"


@dataclass
class DecisionResult:

    decision: Decision

    confidence: str

    reason: str


class DecisionEngine:

    def evaluate(

        self,

        sky_score,

        market_cycle,

        portfolio_weight,

        max_weight=0.25,

        cash_ratio=0.10

    ):

        decision = Decision.HOLD

        reason = []

        if sky_score.percentage >= 90:

            decision = Decision.STRONG_BUY

        elif sky_score.percentage >= 75:

            decision = Decision.BUY

        elif sky_score.percentage >= 60:

            decision = Decision.ACCUMULATE

        elif sky_score.percentage >= 40:

            decision = Decision.HOLD

        elif sky_score.percentage >= 20:

            decision = Decision.REDUCE

        else:

            decision = Decision.SELL

        if market_cycle == "BEAR":

            if decision in (
                Decision.STRONG_BUY,
                Decision.BUY
            ):
                decision = Decision.ACCUMULATE

            reason.append("Bear market adjustment")

        elif market_cycle == "ACCUMULATION":

            if decision == Decision.BUY:
                decision = Decision.STRONG_BUY

            reason.append("Accumulation phase")

        if portfolio_weight > max_weight:

            if decision == Decision.STRONG_BUY:
                decision = Decision.BUY

            elif decision == Decision.BUY:
                decision = Decision.HOLD

            reason.append("Asset overweight")

        if cash_ratio < 0.05:

            if decision in (
                Decision.STRONG_BUY,
                Decision.BUY
            ):
                decision = Decision.HOLD

            reason.append("Low cash reserve")

        return DecisionResult(

            decision=decision,

            confidence=sky_score.confidence,

            reason=", ".join(reason) if reason else "Score based"

        )
