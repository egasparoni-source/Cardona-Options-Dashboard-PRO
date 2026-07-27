from src.market.market_data import MarketData


class MarketStep:

    @staticmethod
    def run(context):

        symbol = context.get("symbol")
        timeframe = context.get("timeframe")

        df = MarketData.get_price(symbol, timeframe)

        context.set("market", df)

        return context