class Scoring:

    @staticmethod
    def calculate(trend, momentum, volatility, price_above_vwap):

        score = 0

        # Tendencia
        if trend == "BULLISH":
            score += 30
        elif trend == "BEARISH":
            score += 30

        # Momentum
        if momentum == "STRONG BULLISH":
            score += 30
        elif momentum == "STRONG BEARISH":
            score += 30

        # Volatilidad
        if volatility == "NORMAL":
            score += 20
        elif volatility == "LOW":
            score += 10

        # VWAP
        if price_above_vwap:
            score += 20

        return score