from data.market import MarketData
from data.fact import Fact


def market_data_to_facts(market: MarketData) -> list[Fact]:
    facts = []

    if market.price is not None and market.ema200 is not None:
        facts.append(
            Fact(
                id="PRICE_ABOVE_EMA200",
                value=market.price > market.ema200
            )
        )

    return facts
