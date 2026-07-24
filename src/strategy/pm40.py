from src.strategy.base_strategy import BaseStrategy
from src.support.support_engine import SupportEngine

class PM40Strategy(BaseStrategy):

    name = "PM40"

    @staticmethod
    def analyze(df, mtf):

        if df is None or df.empty:
            return None

        last = df.iloc[-1]

        score = 0

        signal = "WAIT"

        # ------------------------
        # Tendencia principal
        # ------------------------

        trend_ok = (
            last["EMA20"] >
            last["EMA40"] >
            last["EMA100"] >
            last["EMA200"]
        )

        if trend_ok:
            score += 40

        # ------------------------
        # MTF Alignment
        # ------------------------

        if (
            mtf["1D"]["trend"] == "BULLISH"
        ):
            score += 20

        if (
            mtf["1W"]["trend"] == "BULLISH"
        ):
            score += 20

        # ------------------------
        # Pullback EMA40
        # ------------------------

        distance = abs(
            last["Close"] - last["EMA40"]
        ) / last["EMA40"]

        if distance <= 0.01:
            score += 10

        # ------------------------
        # Confirmación vela
        # ------------------------

        if last["Close"] > last["Open"]:
            score += 10

        # ------------------------
        # Señal
        # ------------------------

        if score >= 80:
            signal = "BUY"
        support = SupportEngine.analyze(df)

        return {

         "strategy": "PM40",

         "signal": signal,

         "score": score,

         "trend_ok": trend_ok,

         "entry": support["entry"],

         "support": support["support"],

         "resistance": support["resistance"],

         "stop": support["stop"],

         "target1": support["target1"],

         "target2": support["target2"],

         "risk_reward": support["risk_reward"]

    }   