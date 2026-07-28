from pprint import pprint

from src.core.trading_engine import TradingEngine

context = TradingEngine.run("SPY", "1h")

print("\n===== CONTEXT =====\n")

pprint(context.keys())

print("\n===== SIGNAL =====\n")

pprint(context["signal"])

print("\n===== MTF =====\n")

pprint(context["mtf"])
print("\n===== STRUCTURE =====\n")
pprint(context["structure"])

print("\n===== PM40 =====\n")
pprint(context["pm40"])

print("\n===== RISK =====\n")
pprint(context["risk"])
print("\n===== TRADE =====\n")
pprint(context["trade"])

print("\n===== RECOMMENDATION =====\n")
pprint(context["recommendation"])

print("\n===== OPTIONS =====\n")
pprint(context["options"])