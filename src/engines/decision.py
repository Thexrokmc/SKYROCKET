from dataclasses import dataclass


@dataclass(frozen=True)
class Decision:
    action: str
    buy_score: int
    sell_score: int
    confidence: int
    reasons: list[str]
