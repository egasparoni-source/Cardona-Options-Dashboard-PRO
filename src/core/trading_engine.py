from src.core.pipeline import Pipeline
from src.core.trading_context import TradingContext

from src.core.steps.market_step import MarketStep
from src.core.steps.indicator_step import IndicatorStep
from src.core.steps.signal_step import SignalStep
from src.core.steps.mtf_step import MTFStep


class TradingEngine:

    @staticmethod
    def run(symbol="SPY", timeframe="1h"):

        context = TradingContext(symbol, timeframe)

        pipeline = Pipeline()

        pipeline.add(MarketStep.run)
        pipeline.add(IndicatorStep.run)
        pipeline.add(SignalStep.run)
        pipeline.add(MTFStep.run)

        context = pipeline.run(context)

        return context.export()