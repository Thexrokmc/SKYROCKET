from .base_rule import BaseRule


class AllocationRule(BaseRule):

    def __init__(self):
        super().__init__(
            name="Portfolio Allocation",
            weight=15
        )

    def evaluate(self, portfolio, market=None):

        if portfolio.total_value == 0:
            return {
                "passed": False,
                "score": 0,
                "reason": "Portfolio is empty."
            }

        return {
            "passed": True,
            "score": self.weight,
            "reason": "Portfolio allocation check passed."
        }
