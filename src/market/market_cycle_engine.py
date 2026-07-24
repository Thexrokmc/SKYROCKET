from dataclasses import dataclass
from enum import Enum


class MarketPhase(Enum):
    ACCUMULATION = "ACCUMULATION"
    BULL = "BULL"
    EUPHORIA = "EUPHORIA"
    DISTRIBUTION = "DISTRIBUTION"
    BEAR = "BEAR"
    TRANSITION = "TRANSITION"


@dataclass
class MarketCycleResult:
    phase: MarketPhase
    confidence: float
    reason: str


class MarketCycleEngine:

    def detect(
        self,
        btc_price,
        ema200,
        rsi,
        macd
    ) -> str:

        return self.evaluate(
            btc_price=btc_price,
            ema200=ema200,
            ema50=ema200,
            rsi=rsi,
            macd=macd,
            fear_greed=50
        ).phase.value

    def evaluate(
        self,
        btc_price,
        ema200,
        ema50,
        rsi,
        macd,
        fear_greed=50
    ) -> MarketCycleResult:

        # Ισχυρή ανοδική αγορά
        if (
            btc_price > ema200
            and ema50 > ema200
            and rsi >= 75
            and macd > 0
        ):
            return MarketCycleResult(
                phase=MarketPhase.EUPHORIA,
                confidence=0.95,
                reason="Strong bullish trend with overheated momentum"
            )

        # Κανονικό Bull Market
        if (
            btc_price > ema200
            and ema50 > ema200
            and rsi >= 55
            and macd > 0
        ):
            return MarketCycleResult(
                phase=MarketPhase.BULL,
                confidence=0.90,
                reason="Healthy bullish trend"
            )

        # Φάση συσσώρευσης
        if (
            btc_price > ema200
            and rsi >= 45
        ):
            return MarketCycleResult(
                phase=MarketPhase.ACCUMULATION,
                confidence=0.80,
                reason="Price above EMA200 with improving momentum"
            )

        # Bear λόγω φόβου
        if fear_greed < 25:
            return MarketCycleResult(
                phase=MarketPhase.BEAR,
                confidence=0.85,
                reason="Extreme fear"
            )

        # Bear λόγω τεχνικής εικόνας
        if (
            btc_price < ema200
            and rsi < 40
        ):
            return MarketCycleResult(
                phase=MarketPhase.BEAR,
                confidence=0.90,
                reason="Price below EMA200"
            )

        # Μεταβατική περίοδος
        return MarketCycleResult(
            phase=MarketPhase.TRANSITION,
            confidence=0.60,
            reason="Mixed market conditions"
        )
