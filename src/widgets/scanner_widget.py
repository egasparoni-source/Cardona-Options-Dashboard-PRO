import customtkinter as ctk

from src.scanner.scanner_engine import ScannerEngine


class ScannerWidget(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="SCANNER PRO",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.box = ctk.CTkTextbox(
            self,
            width=320,
            height=350
        )

        self.box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.load_scanner()

    def load_scanner(self):

        scanner = ScannerEngine.scan()

        texto = ""

        for stock in scanner:

            signal = stock["signal"]

            if signal == "BUY":
                icon = "🟢"

            elif signal == "SELL":
                icon = "🔴"

            else:
                icon = "🟡"

            texto += (
                f"{icon} "
                f"{stock['symbol']:6}"
                f" Score:{stock['score']:3}"
                f" RR:{stock['rr']:.1f}\n"
            )

        self.box.insert("1.0", texto)
        self.box.configure(state="disabled")