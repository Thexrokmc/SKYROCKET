# SKYROCKET Rules

## Rule 1
Name: Price Above EMA200

Weight: 20

Facts:
- PRICE_ABOVE_EMA200

Passes when:
- PRICE_ABOVE_EMA200 == True

Impact:
- Buy Score +20

Reason:
- Long-term trend is bullish.


---

## Rule 2
Name: Price Above EMA50

Weight: 10

Facts:
- PRICE_ABOVE_EMA50

Passes when:
- PRICE_ABOVE_EMA50 == True

Impact:
- Buy Score +10

Reason:
- Medium-term trend is bullish.


---

## Rule 3
Name: RSI Oversold

Weight: 15

Facts:
- RSI_OVERSOLD

Passes when:
- RSI_OVERSOLD == True

Impact:
- Buy Score +15

Reason:
- Asset may be undervalued.


---

## Rule 4
Name: RSI Overbought

Weight: 15

Facts:
- RSI_OVERBOUGHT

Passes when:
- RSI_OVERBOUGHT == True

Impact:
- Sell Score +15

Reason:
- Asset may be overextended.


---

## Rule 5
Name: MACD Bullish Cross

Weight: 15

Facts:
- MACD_BULLISH_CROSS

Passes when:
- MACD_BULLISH_CROSS == True

Impact:
- Buy Score +15

Reason:
- Bullish momentum confirmed.


---

## Rule 6
Name: MACD Bearish Cross

Weight: 15

Facts:
- MACD_BEARISH_CROSS

Passes when:
- MACD_BEARISH_CROSS == True

Impact:
- Sell Score +15

Reason:
- Bearish momentum confirmed.


---

## Rule 7
Name: Portfolio Allocation

Weight: 20

Purpose:
- Prevent overexposure to a single asset.


---

## Rule 8
Name: DCA Opportunity

Weight: 20

Purpose:
- Detect high-quality long-term accumulation opportunities.


---

## Rule 9
Name: Profit Taking

Weight: 20

Purpose:
- Suggest partial profit taking during strong rallies.


---

## Rule 10
Name: Risk Control

Weight: 30

Purpose:
- Reduce portfolio risk before maximizing returns.
