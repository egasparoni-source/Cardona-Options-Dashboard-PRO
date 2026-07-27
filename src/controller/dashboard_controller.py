from src import market, trade
from src.market.market_data import MarketData
from src.indicators.indicator_engine import IndicatorEngine
from src.strategy import pm40
from src.timeframes.timeframe_engine import TimeFrameEngine
from src.strategy.pm40 import PM40Strategy
from src.risk.risk_manager import RiskManager
from src.signals.signal_engine import SignalEngine
from src.market.market_session import MarketSession
from src.trade.trade_setup_engine import TradeSetupEngine
from src.trade.recommendation_engine import RecommendationEngine
from src.options.options_engine import OptionsEngine

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
        trade = TradeSetupEngine.build(
           pm40,
           structure,
           risk
        )

        recommendation = RecommendationEngine.analyze(trade)
        trade["action"] = recommendation["action"]
        trade["confidence"] = recommendation["confidence"]
        signal = SignalEngine.analyze(datos)
        market = MarketSession.get_status()
        options = OptionsEngine.analyze(
                trade,
                risk,
                timeframe="1h"
        )


        return {
            "symbol": symbol,
            "market": market,            
            "data": datos,
            "mtf": mtf,
            "pm40": pm40,
            "risk": risk,
            "trade": trade,

            "recommendation": recommendation,
            "options": options,
            "signal": signal
        }
            