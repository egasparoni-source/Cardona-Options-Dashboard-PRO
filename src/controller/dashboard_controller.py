from src.market.market_data import MarketData
from src.indicators.indicator_engine import IndicatorEngine
from src.timeframes.timeframe_engine import TimeFrameEngine
from src.strategy.pm40 import PM40Strategy
from src.risk.risk_manager import RiskManager
from src.signals.signal_engine import SignalEngine


class DashboardController:

    @staticmethod
    def load(symbol="SPY", capital=5000):

        datos = MarketData.get_price(symbol)

        if datos is None:
            return None

        datos = IndicatorEngine.calculate(datos)

        mtf = TimeFrameEngine.analyze(symbol)

        pm40 = PM40Strategy.analyze(datos, mtf)

        risk = RiskManager.analyze(
            capital=capital,
            risk_percent=1,
            entry=pm40["entry"],
            stop=pm40["stop"],
            target=pm40["target1"]
        )

        signal = SignalEngine.analyze(datos)

        return {
            "symbol": symbol,
            "data": datos,
            "mtf": mtf,
            "pm40": pm40,
            "risk": risk,
            "signal": signal
        }