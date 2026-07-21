class AnalysisResult:

    def __init__(

        self,

        symbol,

        price,

        score,

        market_cycle,

        decision,

        reasons=None

    ):

        self.symbol = symbol

        self.price = price

        self.score = score

        self.market_cycle = market_cycle

        self.decision = decision

        self.reasons = reasons or []

    def __repr__(self):

        return (

            f"AnalysisResult("

            f"symbol={self.symbol}, "

            f"price={self.price}, "

            f"score={self.score}, "

            f"market_cycle={self.market_cycle}, "

            f"decision={self.decision}"

            f")"

        )
