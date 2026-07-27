class TradeSetupEngine:

    @staticmethod
    def build(pm40, structure, risk):

        if pm40 is None:
            return None

        return {

            "strategy": pm40["strategy"],

            "signal": pm40["signal"],

            "score": pm40["score"],

            "trend": structure["trend"],

            "momentum": structure["momentum"],

            "volatility": structure["volatility"],

            "entry": pm40["entry"],

            "stop": pm40["stop"],

            "target1": pm40["target1"],

            "target2": pm40["target2"],

            "risk_reward": pm40["risk_reward"],

            "shares": risk["shares"],

            "capital": risk["capital"]
        }