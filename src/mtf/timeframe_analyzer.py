from src.market.market_data import MarketData
from src.indicators.indicator_engine import IndicatorEngine
from src.strategy.pm40 import PM40Strategy


class TimeframeAnalyzer:

    @staticmethod
    def analyze(symbol, interval):

        data = MarketData.get_price(symbol, interval=interval)

        if data is None or len(data) < 50:
            return None

        data = IndicatorEngine.calculate(data)

        pm40 = PM40Strategy.analyze(data)

        return {
            "interval": interval,
            "signal": pm40["signal"],
            "score": pm40["score"],
            "entry": pm40["entry"]
        }