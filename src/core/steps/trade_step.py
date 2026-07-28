from src.trade.trade_setup_engine import TradeSetupEngine


class TradeStep:

    @staticmethod
    def run(context):

        pm40 = context.get("pm40")
        structure = context.get("structure")
        risk = context.get("risk")

        if None in (pm40, structure, risk):
            return context

        trade = TradeSetupEngine.build(
            pm40,
            structure,
            risk
        )

        context.set("trade", trade)

        return context