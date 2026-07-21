class MarketCycleEngine:

    def detect(

        self,

        btc_price,

        ema200,

        rsi,

        macd

    ):

        if (

            btc_price > ema200

            and

            rsi > 60

            and

            macd > 0

        ):

            return "BULL"

        elif (

            btc_price > ema200

            and

            rsi >= 45

        ):

            return "ACCUMULATION"

        elif (

            btc_price < ema200

            and

            rsi < 40

        ):

            return "BEAR"

        else:

            return "TRANSITION"
