class RuleResult:

    def __init__(
        self,
        name: str,
        passed: bool,
        weight: int,
        description: str = ""
    ):

        self.name = name
        self.passed = passed
        self.weight = weight
        self.description = description

    def __repr__(self):

        status = "PASS" if self.passed else "FAIL"

        return (
            f"{self.name} | "
            f"{status} | "
            f"{self.weight} | "
            f"{self.description}"
        )
