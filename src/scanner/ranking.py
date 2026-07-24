class Ranking:

    @staticmethod
    def calculate(df, analysis):

        if df is None or df.empty or analysis is None:
            return 0

        score = 0

        last = df.iloc[-1]

        # Tendencia
        if analysis["trend"] == "BULLISH":
            score += 30
        elif analysis["trend"] == "BEARISH":
            score += 30

        # Señal
        if analysis["signal"] == "BUY":
            score += 30
        elif analysis["signal"] == "SELL":
            score += 30

        # RSI
        rsi = last["RSI"]

        if 45 <= rsi <= 65:
            score += 20

        # Precio respecto al VWAP
        if last["Close"] > last["VWAP"]:
            score += 20

        return score