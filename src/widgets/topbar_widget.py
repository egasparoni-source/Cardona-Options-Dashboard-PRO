import customtkinter as ctk


class TopBarWidget(ctk.CTkFrame):

    def __init__(self, master, market):

        super().__init__(master, height=70)

        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)

        # -----------------------------------
        # Título
        # -----------------------------------

        self.title = ctk.CTkLabel(
            self,
            text="CARDONA OPTIONS DASHBOARD PRO",
            font=("Arial", 22, "bold")
        )

        self.title.grid(
            row=0,
            column=0,
            padx=20,
            pady=15,
            sticky="w"
        )

        # -----------------------------------
        # Symbol
        # -----------------------------------

        self.symbol = ctk.CTkOptionMenu(
            self,
            values=[
                "SPY",
                "QQQ",
                "AAPL",
                "MSFT",
                "NVDA",
                "AMD",
                "META",
                "TSLA",
                "AMZN"
            ]
        )

        self.symbol.set("SPY")

        self.symbol.grid(
            row=0,
            column=1,
            padx=10
        )

        # -----------------------------------
        # TimeFrame
        # -----------------------------------

        self.timeframe = ctk.CTkOptionMenu(
            self,
            values=[
                "1m",
                "5m",
                "15m",
                "30m",
                "1h",
                "4h",
                "1d"
            ]
        )

        self.timeframe.set("5m")

        self.timeframe.grid(
            row=0,
            column=2,
            padx=10
        )

        # -----------------------------------
        # Refresh
        # -----------------------------------

        self.refresh = ctk.CTkButton(
            self,
            text="🔄 Refresh"
        )

        self.refresh.grid(
            row=0,
            column=3,
            padx=10
        )

        # -----------------------------------
        # Market
        # -----------------------------------

        self.market = ctk.CTkLabel(
            self,
            text=(
                f"{market['icon']} {market['status']}\n"
                f"{market['time']} NY"
            ),
            font=("Arial", 14, "bold"),
            justify="center"
        )

        self.market.grid(
            row=0,
            column=4,
            padx=20
        )