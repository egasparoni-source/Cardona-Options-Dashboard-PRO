import yfinance as yf


class MarketData:

    @staticmethod
    def get_price(symbol="SPY", interval="1h"):

        try:

            ticker = yf.Ticker(symbol)

            # Configuración automática del período según el timeframe
            if interval == "5m":
                period = "5d"

            elif interval == "15m":
                period = "30d"

            elif interval == "1h":
                period = "2y"

            elif interval == "1d":
                period = "10y"

            elif interval == "1wk":
                period = "10y"

            elif interval == "1mo":
                period = "max"

            else:
                period = "1y"

            data = ticker.history(
                period=period,
                interval=interval,
                auto_adjust=True
            )

            if data.empty:
                return None

            return data

        except Exception as e:

            print(f"MarketData Error ({symbol}): {e}")

            return None