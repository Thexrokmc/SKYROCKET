from data.data_provider import DataProvider

from data.fact_generator import (
    market_data_to_facts
)

from rules.rule_engine import RuleEngine

from rules.price_above_ema200_rule import (
    PriceAboveEMA200Rule
)

from rules.price_above_ema50_rule import (
    PriceAboveEMA50Rule
)

from rules.rsi_oversold_rule import (
    RSIOversoldRule
)

from rules.macd_bullish_rule import (
    MACDBullishRule
)

from rules.macd_bearish_rule import (
    MACDBearishRule
)

from rules.allocation_rule import (
    AllocationRule
)

from rules.trend_rule import (
    TrendRule
)

from decision.decision_engine import (
    DecisionEngine
)


provider = DataProvider()

market = provider.load_market_data()

facts = market_data_to_facts(
    market
)

rule_engine = RuleEngine([

    TrendRule(),

    PriceAboveEMA200Rule(),
    PriceAboveEMA50Rule(),

    RSIOversoldRule(),

    MACDBullishRule(),
    MACDBearishRule(),

    AllocationRule(),

])

results = rule_engine.evaluate(
    facts
)

decision_engine = DecisionEngine()

decision = decision_engine.decide(
    results
)

print()

print("===== MARKET =====")
print(vars(market))

print()

print("===== RULE RESULTS =====")

for result in results:
    print(result)

print()

print("===== DECISION =====")
print(decision)
