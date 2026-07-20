from dataclasses import dataclass


@dataclass(frozen=True)
class RuleResult:
    name: str
    passed: bool
    weight: int
