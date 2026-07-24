class TrendEngine:

    @staticmethod
    def analyze(df):

        if df is None or df.empty:
            return None

        last = df.iloc[-1]

        ema20 = last["EMA20"]
        ema40 = last["EMA40"]
        ema100 = last["EMA100"]
        ema200 = last["EMA200"]
        price = last["Close"]

        # Tendencia principal
        if ema20 > ema40 > ema100 > ema200:

            trend = "BULLISH"

        elif ema20 < ema40 < ema100 < ema200:

            trend = "BEARISH"

        else:

            trend = "SIDEWAYS"

        # Fortaleza de la tendencia
        strength = 0

        if trend != "SIDEWAYS":
            strength += 40

        if price > ema20:
            strength += 15

        if price > ema40:
            strength += 15

        if price > ema100:
            strength += 15

        if price > ema200:
            strength += 15

        return {

            "trend": trend,

            "strength": strength,

            "price": price,

            "ema20": ema20,

            "ema40": ema40,

            "ema100": ema100,

            "ema200": ema200
        }