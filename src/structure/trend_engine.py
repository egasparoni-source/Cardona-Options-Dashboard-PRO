class TrendEngine:

    @staticmethod
    def analyze(data):

        last = data.iloc[-1]

        ema20 = last["EMA20"]
        ema40 = last["EMA40"]
        ema100 = last["EMA100"]
        ema200 = last["EMA200"]

        price = last["Close"]

        if price > ema20 > ema40 > ema100 > ema200:
            return "STRONG_BULL"

        elif price > ema40 > ema100 > ema200:
            return "BULL"

        elif price < ema20 < ema40 < ema100 < ema200:
            return "STRONG_BEAR"

        elif price < ema40 < ema100 < ema200:
            return "BEAR"

        return "NEUTRAL"