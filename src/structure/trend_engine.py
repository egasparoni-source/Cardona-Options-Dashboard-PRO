class TrendEngine:

    @staticmethod
    def analyze(data):

        ema20 = data["EMA20"].iloc[-1]
        ema50 = data["EMA50"].iloc[-1]
        ema200 = data["EMA200"].iloc[-1]

        price = data["Close"].iloc[-1]

        if price > ema20 > ema50 > ema200:
            trend = "STRONG_BULL"

        elif price > ema50:
            trend = "BULL"

        elif price < ema20 < ema50 < ema200:
            trend = "STRONG_BEAR"

        else:
            trend = "NEUTRAL"

        return trend