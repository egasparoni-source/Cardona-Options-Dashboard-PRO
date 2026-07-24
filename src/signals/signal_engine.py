from src.trend.trend_engine import TrendEngine
from src.signals.momentum import Momentum
from src.signals.volatility import Volatility
from src.signals.scoring import Scoring


class SignalEngine:

    @staticmethod
    def analyze(df):

        if df is None or df.empty:
            return None

        trend_data = TrendEngine.analyze(df)
        trend = trend_data["trend"]
        
        momentum = Momentum.analyze(df)
        volatility = Volatility.analyze(df)

        price = df["Close"].iloc[-1]
        vwap = df["VWAP"].iloc[-1]

        price_above_vwap = price > vwap

        confidence = Scoring.calculate(
            trend,
            momentum,
            volatility,
            price_above_vwap
        )

        # Señal principal
        if trend == "BULLISH" and momentum == "STRONG BULLISH":
            signal = "BUY CALL"

        elif trend == "BEARISH" and momentum == "STRONG BEARISH":
            signal = "BUY PUT"

        else:
            signal = "WAIT"

        return {
            "signal": signal,
            "confidence": confidence,
            "trend": trend,
            "momentum": momentum,
            "volatility": volatility
        }