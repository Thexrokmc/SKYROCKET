from dataclasses import dataclass
from typing import Callable, List


@dataclass
class RuleResult:

    name: str
    passed: bool
    weight: int
    score: int
    message: str


class Rule:

    def __init__(
        self,
        name: str,
        weight: int,
        evaluator: Callable
    ):

        self.name = name
        self.weight = weight
        self.evaluator = evaluator

    def evaluate(self, facts):

        passed = self.evaluator(facts)

        return RuleResult(

            name=self.name,

            passed=passed,

            weight=self.weight,

            score=self.weight if passed else 0,

            message="PASS" if passed else "FAIL"

        )


class RulesEngine:

    def __init__(self):

        self.rules: List[Rule] = []

    def register(self, rule: Rule):

        self.rules.append(rule)

    def evaluate(self, facts):

        return [

            rule.evaluate(facts)

            for rule in self.rules

        ]

    def total_score(self, results):

        return sum(

            r.score

            for r in results

        )

    def max_score(self):

        return sum(

            r.weight

            for r in self.rules

        )
