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

        if len(values) < 35:
            return None, None, None

        multiplier12 = 2 / (12 + 1)
        multiplier26 = 2 / (26 + 1)
        multiplier9 = 2 / (9 + 1)

        ema12 = values[0]
        ema26 = values[0]

        macd_values = []

        for price in values:

            ema12 = (price - ema12) * multiplier12 + ema12
            ema26 = (price - ema26) * multiplier26 + ema26

            macd_values.append(
                ema12 - ema26
            )

        signal = macd_values[0]

        for value in macd_values:

            signal = (
                (value - signal) * multiplier9
            ) + signal

        macd = macd_values[-1]

        histogram = macd - signal

        return (
            macd,
            signal,
            histogram
        )
