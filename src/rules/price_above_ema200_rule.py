from rules.base_rule import BaseRule
from data.fact_ids import PRICE_ABOVE_EMA200


class PriceAboveEMA200Rule(BaseRule):

    def evaluate(self, facts) -> bool:
        return facts.get(PRICE_ABOVE_EMA200, False)
