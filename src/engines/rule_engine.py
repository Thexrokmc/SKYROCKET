from rules.rule_result import RuleResult


class RuleEngine:

    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self, facts: dict) -> list[RuleResult]:
        results = []

        for rule in self.rules:
            results.append(
                rule.evaluate(facts)
            )

        return results
