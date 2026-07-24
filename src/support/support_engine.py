class SupportEngine:

    @staticmethod
    def analyze(df):

        if df is None or df.empty:
            return None

        # Últimas 20 velas
        recent = df.tail(20)

        support = recent["Low"].min()

        resistance = recent["High"].max()

        last = recent.iloc[-1]

        entry = last["Close"]

        stop = support

        risk = entry - stop

        target1 = entry + (risk * 2)

        target2 = entry + (risk * 3)

        rr = round((target1 - entry) / risk, 2) if risk > 0 else 0

        return {

            "entry": round(entry, 2),

            "support": round(support, 2),

            "resistance": round(resistance, 2),

            "stop": round(stop, 2),

            "target1": round(target1, 2),

            "target2": round(target2, 2),

            "risk_reward": rr
        }