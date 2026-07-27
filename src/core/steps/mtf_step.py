from src.timeframes.timeframe_engine import TimeFrameEngine


class MTFStep:

    @staticmethod
    def run(context):

        symbol = context.get("symbol")

        mtf = TimeFrameEngine.analyze(symbol)

        context.set("mtf", mtf)

        return context