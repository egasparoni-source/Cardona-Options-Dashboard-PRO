class VolatilityEngine:

    @staticmethod
    def analyze(data):

        atr = data["ATR"].iloc[-1]

        price = data["Close"].iloc[-1]

        volatility = atr / price

        if volatility > 0.03:
            return "HIGH"

        elif volatility > 0.015:
            return "NORMAL"

        return "LOW"