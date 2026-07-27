from pprint import pprint

from src.core.trading_engine import TradingEngine

context = TradingEngine.run("SPY", "1h")

print("\n===== CONTEXT =====\n")

pprint(context.keys())

print("\n===== SIGNAL =====\n")

pprint(context["signal"])

print("\n===== MTF =====\n")

pprint(context["mtf"])