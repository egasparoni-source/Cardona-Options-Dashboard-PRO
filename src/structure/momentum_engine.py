class MomentumEngine:

    @staticmethod
    def analyze(data):

        rsi = data["RSI"].iloc[-1]
        macd = data["MACD"].iloc[-1]

        if rsi > 60 and macd > 0:
            return "STRONG"

        elif rsi > 50:
            return "GOOD"

        elif rsi > 40:
            return "WEAK"

        return "NEGATIVE"