from pprint import pprint

from src.scanner.market_scanner import MarketScanner
from src.scanner.scanner_engine import ScannerEngine
from src.scanner.ranking import Ranking


symbols = MarketScanner.default_watchlist()

print(f"\nEscaneando {len(symbols)} activos...\n")

results = ScannerEngine.scan(symbols)

ranking = Ranking.sort(results)

print("\n===== RANKING =====\n")

for item in ranking:

    pprint({

        "symbol": item["symbol"],

        "score": item["trade"]["score"],

        "signal": item["trade"]["signal"],

        "action": item["recommendation"]["action"]

    })