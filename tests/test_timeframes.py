from pprint import pprint

from src.timeframes.timeframe_engine import TimeFrameEngine

resultado = TimeFrameEngine.analyze("SPY")

print("\n========== CARDONA MTF ENGINE ==========\n")

pprint(resultado)

print("\n========================================")