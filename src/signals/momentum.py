class Momentum:

    @staticmethod
    def analyze(df):

        if df is None or df.empty:
            return "UNKNOWN"

        last = df.iloc[-1]

        rsi = last["RSI"]

        macd = last["MACD"]

        signal = last["MACD_SIGNAL"]

        # Momentum Alcista
        if rsi >= 55 and macd > signal:
            return "STRONG BULLISH"

        # Momentum Bajista
        elif rsi <= 45 and macd < signal:
            return "STRONG BEARISH"

        return "NEUTRAL"