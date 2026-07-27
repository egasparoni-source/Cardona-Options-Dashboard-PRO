from src.indicators.indicator_engine import IndicatorEngine


class IndicatorStep:

    @staticmethod
    def run(context):

        df = context.get("market")

        if df is None:
            return context

        df = IndicatorEngine.calculate(df)

        context.set("market", df)

        return context