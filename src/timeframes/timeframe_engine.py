from src.market.market_data import MarketData
from src.indicators.indicator_engine import IndicatorEngine
from src.trend.trend_engine import TrendEngine


class TimeFrameEngine:

    TIMEFRAMES = {
        "1H": "1h",
        "1D": "1d",
        "1W": "1wk",
        "1M": "1mo"
    }

    @staticmethod
    def analyze(symbol):

        results = {}

        for name, interval in TimeFrameEngine.TIMEFRAMES.items():

            df = MarketData.get_price(symbol, interval)

            if df is None:
                continue

            df = IndicatorEngine.calculate(df)

            trend = TrendEngine.analyze(df)

            results[name] = trend

        return results