from src.market.market_data import MarketData


class MarketScanner:

    DEFAULT_SYMBOLS = [
        "SPY",
        "QQQ",
        "AAPL",
        "MSFT",
        "NVDA",
        "META",
        "AMD",
        "AMZN",
        "GOOGL",
        "TSLA",
        "NFLX"
    ]

    @staticmethod
    def scan(symbols=None):

        if symbols is None:
            symbols = MarketScanner.DEFAULT_SYMBOLS

        market = {}

        for symbol in symbols:

            try:

                data = MarketData.get_price(symbol)

                if data is not None and not data.empty:

                    market[symbol] = data

            except Exception as e:

                print(f"Error descargando {symbol}: {e}")

        return market