from src.options.options_engine import OptionsEngine


class OptionsStep:

    @staticmethod
    def run(context):

        trade = context.get("trade")
        risk = context.get("risk")
        recommendation = context.get("recommendation")

        if None in (trade, risk, recommendation):
            return context

        options = OptionsEngine.analyze(
            trade,
            risk,
            recommendation,
            timeframe=context.get("timeframe")
        )

        context.set("options", options)

        return context