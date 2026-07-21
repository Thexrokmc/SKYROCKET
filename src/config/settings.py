class Settings:

    # ==========================
    # Portfolio
    # ==========================

    BASE_CURRENCY = "EUR"

    MAX_ASSET_ALLOCATION = 20.0

    MIN_ASSET_ALLOCATION = 5.0

    # ==========================
    # SkyScore
    # ==========================

    BUY_SCORE = 80

    ACCUMULATE_SCORE = 60

    HOLD_SCORE = 40

    # ==========================
    # Indicators
    # ==========================

    EMA_FAST = 50

    EMA_SLOW = 200

    RSI_PERIOD = 14

    RSI_BULLISH = 50

    RSI_OVERSOLD = 30

    RSI_OVERBOUGHT = 70

    MACD_FAST = 12

    MACD_SLOW = 26

    MACD_SIGNAL = 9

    # ==========================
    # Timeframes
    # ==========================

    DAILY = "1d"

    H4 = "4h"

    H1 = "1h"

    M15 = "15m"

    # ==========================
    # Market Cycle
    # ==========================

    BULL_RSI = 60

    BEAR_RSI = 40

    # ==========================
    # Risk Management
    # ==========================

    MAX_PORTFOLIO_RISK = 100.0

    # ==========================
    # DCA
    # ==========================

    STRONG_DCA_SCORE = 90

    BUY_DCA_SCORE = 80

    SMALL_DCA_SCORE = 60

    # ==========================
    # Profit Taking
    # ==========================

    SMALL_PROFIT_PERCENT = 10

    NORMAL_PROFIT_PERCENT = 20

    REDUCE_POSITION_PERCENT = 35

    EXIT_POSITION_PERCENT = 50
