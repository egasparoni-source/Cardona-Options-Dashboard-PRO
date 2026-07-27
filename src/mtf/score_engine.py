class ScoreEngine:

    @staticmethod
    def calculate(pm40):

        score = pm40.get("score", 0)

        signal = pm40.get("signal", "WAIT")

        if score >= 90:
            trend = "Strong Bullish"

        elif score >= 70:
            trend = "Bullish"

        elif score >= 50:
            trend = "Neutral"

        elif score >= 30:
            trend = "Bearish"

        else:
            trend = "Strong Bearish"

        return {
            "score": score,
            "signal": signal,
            "trend": trend
        }