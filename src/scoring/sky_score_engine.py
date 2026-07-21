from dataclasses import dataclass
from typing import List

from rules.rules_engine import RuleResult


@dataclass
class SkyScore:

    score: int
    max_score: int
    percentage: float

    rating: str

    confidence: str


class SkyScoreEngine:

    def calculate(

        self,

        results: List[RuleResult]

    ) -> SkyScore:

        total = sum(

            r.score

            for r in results

        )

        maximum = sum(

            r.weight

            for r in results

        )

        percentage = (

            total / maximum * 100

            if maximum

            else 0

        )

        if percentage >= 90:

            rating = "STRONG BUY"

            confidence = "VERY HIGH"

        elif percentage >= 75:

            rating = "BUY"

            confidence = "HIGH"

        elif percentage >= 60:

            rating = "ACCUMULATE"

            confidence = "MEDIUM"

        elif percentage >= 40:

            rating = "HOLD"

            confidence = "LOW"

        elif percentage >= 20:

            rating = "REDUCE"

            confidence = "LOW"

        else:

            rating = "SELL"

            confidence = "HIGH"

        return SkyScore(

            score=total,

            max_score=maximum,

            percentage=round(

                percentage,

                2

            ),

            rating=rating,

            confidence=confidence

        )
