from src.risk.risk_manager import RiskManager


class RiskStep:

    @staticmethod
    def run(context):

        pm40 = context.get("pm40")

        if pm40 is None:
            return context

        risk = RiskManager.analyze(
            capital=5000,
            risk_percent=1,
            entry=pm40["entry"],
            stop=pm40["stop"],
            target=pm40["target1"]
        )

        context.set("risk", risk)

        return context