import customtkinter as ctk

from src.market.market_data import MarketData


class WatchlistWidget(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="WATCHLIST",
            font=("Arial",18,"bold")
        ).pack(pady=10)

        self.box = ctk.CTkTextbox(
            self,
            width=280,
            height=300
        )

        self.box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.refresh()

    def refresh(self):

        self.box.delete("1.0","end")

        symbols = [
            "SPY",
            "QQQ",
            "AAPL",
            "MSFT",
            "NVDA",
            "TSLA",
            "AMD",
            "META"
        ]

        for symbol in symbols:

            try:

                df = MarketData.get_price(symbol)

                if df is None:
                    continue

                price = round(df["Close"].iloc[-1],2)

                self.box.insert(
                    "end",
                    f"{symbol:<6} ${price}\n"
                )

            except:
                pass