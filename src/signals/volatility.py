class Volatility:

    @staticmethod
    def analyze(df):

        if df is None or df.empty:
            return "UNKNOWN"

        atr = df["ATR"].iloc[-1]
        close = df["Close"].iloc[-1]

        if close == 0:
            return "UNKNOWN"

        atr_percent = (atr / close) * 100

        if atr_percent < 1:
            return "LOW"

        elif atr_percent < 3:
            return "NORMAL"

        return "HIGH"