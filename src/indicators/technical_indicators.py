class TechnicalIndicators:

    @staticmethod
    def ema(values: list[float], period: int):

        if len(values) < period:
            return None

        multiplier = 2 / (period + 1)

        ema = sum(values[:period]) / period

        for price in values[period:]:
            ema = (price - ema) * multiplier + ema

        return ema

    @staticmethod
    def rsi(values: list[float], period: int = 14):

        if len(values) < period + 1:
            return None

        gains = []
        losses = []

        for i in range(1, period + 1):

            change = values[i] - values[i - 1]

            if change >= 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period

        if avg_loss == 0:
            return 100

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))

    @staticmethod
    def macd(values: list[float]):

        ema12 = TechnicalIndicators.ema(values, 12)
        ema26 = TechnicalIndicators.ema(values, 26)

        if ema12 is None or ema26 is None:
            return None

        return ema12 - ema26
