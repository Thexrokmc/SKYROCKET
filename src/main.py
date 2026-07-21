from portfolio.portfolio import Portfolio
from data.market import MarketData
from data.fact_generator import market_data_to_facts
from rules.price_above_ema200_rule import PriceAboveEMA200Rule
from rules.price_above_ema50_rule import PriceAboveEMA50Rule
from engines.rule_engine import RuleEngine
from engines.decision_engine import DecisionEngine
from rules.allocation_rule import AllocationRule
from rules.rsi_oversold_rule import RSIOversoldRule

def main():

    print("🚀 SKYROCKET v1.0")
    print("---------------------------")

    portfolio = Portfolio()

    market = MarketData()

    facts = market_data_to_facts(market)

    rule_engine = RuleEngine()

    rule_engine.add_rule(
        AllocationRule()
    )

    results = rule_engine.evaluate(
        facts
    )

    decision = DecisionEngine()

    final = decision.decide(results)

    print(final)


if __name__ == "__main__":
    main()
