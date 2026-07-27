from src.structure.trend_engine import TrendEngine
from src.structure.momentum_engine import MomentumEngine
from src.structure.volatility_engine import VolatilityEngine


class StructureEngine:

    @staticmethod
    def analyze(data):

        trend = TrendEngine.analyze(data)

        momentum = MomentumEngine.analyze(data)

        volatility = VolatilityEngine.analyze(data)

        return {

            "trend": trend,

            "momentum": momentum,

            "volatility": volatility

        }