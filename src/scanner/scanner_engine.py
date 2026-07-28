from src.core.trading_engine import TradingEngine


class ScannerEngine:

    @staticmethod
    def scan(symbols, timeframe="1h"):

        results = []

        for symbol in symbols:

            try:

                context = TradingEngine.run(symbol, timeframe)

                if context is not None:
                    results.append(context)

            except Exception as e:

                print(f"[ERROR] {symbol}: {e}")

        return results