from pprint import pprint

from src.market.market_data import MarketData
from src.indicators.indicator_engine import IndicatorEngine
from src.timeframes.timeframe_engine import TimeFrameEngine
from src.strategy.pm40 import PM40Strategy

symbol = "SPY"

df = MarketData.get_price(symbol, "1d")

df = IndicatorEngine.calculate(df)

mtf = TimeFrameEngine.analyze(symbol)

resultado = PM40Strategy.analyze(df, mtf)

print("\n========== PM40 TEST ==========\n")

pprint(resultado)

print("\n===============================\n")