from src.core import pipeline
from src.core.pipeline import Pipeline
from src.core.trading_context import TradingContext

from src.core.steps.market_step import MarketStep
from src.core.steps.indicator_step import IndicatorStep
from src.core.steps.signal_step import SignalStep
from src.core.steps.mtf_step import MTFStep
from src.core.steps.structure_step import StructureStep
from src.core.steps.pm40_step import PM40Step
from src.core.steps.risk_step import RiskStep
from src.core.steps.trade_step import TradeStep
from src.core.steps.recommendation_step import RecommendationStep
from src.core.steps.options_step import OptionsStep


class TradingEngine:

    @staticmethod
    def run(symbol="SPY", timeframe="1h"):

        context = TradingContext(symbol, timeframe)

        pipeline = Pipeline()

        pipeline.add(MarketStep.run)
        pipeline.add(IndicatorStep.run)
        pipeline.add(SignalStep.run)
        pipeline.add(StructureStep.run)
        pipeline.add(MTFStep.run)
        pipeline.add(PM40Step.run)
        pipeline.add(RiskStep.run)
        pipeline.add(TradeStep.run)
        pipeline.add(RecommendationStep.run)
        pipeline.add(OptionsStep.run)

        context = pipeline.run(context)

        return context.export()