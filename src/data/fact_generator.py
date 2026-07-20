from data.market import MarketData
from data.fact import Fact
from data.fact_ids import PRICE_ABOVE_EMA200, PRICE_ABOVE_EMA50


def add_fact(facts: list[Fact], fact_id: str, value: bool):
    facts.append(
        Fact(
            id=fact_id,
            value=value
        )
    )


def market_data_to_facts(market: MarketData) -> list[Fact]:
    facts = []

    if market.price is not None and market.ema200 is not None:
        add_fact(
            facts,
            PRICE_ABOVE_EMA200,
            market.price > market.ema200
        )

    if market.price is not None and market.ema50 is not None:
        add_fact(
            facts,
            PRICE_ABOVE_EMA50,
            market.price > market.ema50
        )

    return facts
