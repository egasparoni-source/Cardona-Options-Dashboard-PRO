import customtkinter as ctk

from src import dashboard, risk, scanner
from src.controller.dashboard_controller import DashboardController

from src.dashboard import content, topbar
from src.widgets.chart_widget import ChartWidget
from src.widgets.watchlist_widget import WatchlistWidget
from src.widgets.ai_widget import AIWidget
from src.widgets.pm40_widget import PM40Widget
from src.widgets.risk_widget import RiskWidget
from src.widgets.scanner_widget import ScannerWidget
from src.widgets.topbar_widget import TopBarWidget


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Cardona Options Trading Dashboard PRO")
        self.geometry("1700x950")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

       # ==========================
       # TOP BAR
       # ==========================

        topbar = TopBarWidget(
            self,
            dashboard["market"]
        )

        topbar.grid(
          row=0,
          column=0,
          columnspan=2,
          sticky="ew",
          padx=10,
          pady=10
        )

        # ==========================
        # SIDEBAR
        # ==========================

        sidebar = ctk.CTkFrame(
            self,
            width=220
        )

        sidebar.grid(
            row=1,
            column=0,
            sticky="ns"
        )

        buttons = [
            "Dashboard",
            "Scanner",
            "Market",
            "Charts",
            "Risk",
            "Journal",
            "AI",
            "Settings"
        ]

        for text in buttons:

            ctk.CTkButton(
                sidebar,
                text=text,
                width=180
            ).pack(pady=10, padx=15)

        # ==========================
        # CENTRAL PANEL
        # ==========================

        content = ctk.CTkFrame(self)

        content.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        content.grid_columnconfigure(0, weight=3)
        content.grid_columnconfigure(1, weight=1)
        for i in range(4):
            content.grid_rowconfigure(i, weight=1)

        content.grid_rowconfigure(0, weight=2)

        # ==========================
        # LOAD DATA
        # ==========================

        dashboard = DashboardController.load("SPY")

        if dashboard is None:
            return

        # ==========================
        # CHART
        # ==========================

        self.chart = ChartWidget(
           content,
           symbol=dashboard["symbol"]
)

        self.chart.grid(
            row=0,
            column=0,
            rowspan=3,
            sticky="nsew",
            padx=10,
            pady=10
        )
        # ==========================
        # WATCHLIST
        # ==========================
        self.watchlist = WatchlistWidget(content)

        self.watchlist.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )
        
        # ==========================
        # AI SIGNALS
        # ==========================

        self.ai = AIWidget(
            content,
            dashboard["signal"]
        )

        self.ai.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        # ==========================
        # PM40
        # ==========================
        print("\n========== PM40 ==========")
        print(dashboard["pm40"])
        print("==========================\n")
        # ==========================
        # PM40
        # ==========================

        self.pm40 = PM40Widget(
            content,
            dashboard["pm40"]
        )

        self.pm40.grid(
            row=2,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

        # ==========================
        # RISK WINDOW
        # ==========================

        risk = ctk.CTkToplevel(self)
        risk.title("Risk Manager")
        risk.geometry("350x320")

        RiskWidget(
            risk,
            dashboard["risk"]
        ).pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )