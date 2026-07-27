class TradingContext:

    def __init__(self, symbol, timeframe):

        self.data = {

            "symbol": symbol,

            "timeframe": timeframe,

            "market": None,

            "indicators": None,

            "structure": None,

            "signal": None,

            "mtf": None,

            "strategy": None,

            "risk": None,

            "trade": None,

            "recommendation": None,

            "options": None
        }

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def export(self):
        return self.data