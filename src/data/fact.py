from dataclasses import dataclass


@dataclass(frozen=True)
class Fact:
    id: str
    value: bool
