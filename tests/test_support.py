from pprint import pprint

from src.market.market_data import MarketData
from src.indicators.indicator_engine import IndicatorEngine
from src.support.support_engine import SupportEngine

df = MarketData.get_price("SPY", "1d")

df = IndicatorEngine.calculate(df)

resultado = SupportEngine.analyze(df)

print("\n========== SUPPORT ENGINE ==========\n")

pprint(resultado)

print("\n====================================")