class FilterEngine:

    @staticmethod
    def evaluate(df):

        if df is None or df.empty:
            return None

        last = df.iloc[-1]

        ema9 = last["EMA9"]
        ema20 = last["EMA20"]
        ema50 = last["EMA50"]
        rsi = last["RSI"]

        # Tendencia
        if ema9 > ema20 > ema50:
            trend = "BULLISH"
        elif ema9 < ema20 < ema50:
            trend = "BEARISH"
        else:
            trend = "SIDEWAYS"

        # Señal
        if trend == "BULLISH" and rsi < 70:
            signal = "BUY"

        elif trend == "BEARISH" and rsi > 30:
            signal = "SELL"

        else:
            signal = "WAIT"

        return {
            "trend": trend,
            "signal": signal,
            "rsi": round(rsi, 2)
        }