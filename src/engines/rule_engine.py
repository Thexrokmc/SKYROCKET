class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self, portfolio, market=None):
        results = []

        for rule in self.rules:
            results.append(rule.evaluate(portfolio, market))

        return results
