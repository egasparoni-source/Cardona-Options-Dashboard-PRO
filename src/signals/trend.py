class Trend:

    @staticmethod
    def analyze(df):

        if df is None or df.empty:
            return "UNKNOWN"

        last = df.iloc[-1]

        ema9 = last["EMA9"]
        ema20 = last["EMA20"]
        ema50 = last["EMA50"]

        if ema9 > ema20 > ema50:
            return "BULLISH"

        elif ema9 < ema20 < ema50:
            return "BEARISH"

        return "NEUTRAL"