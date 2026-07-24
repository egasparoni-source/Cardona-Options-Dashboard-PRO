import customtkinter as ctk


class AIWidget(ctk.CTkFrame):

    def __init__(self, master, signal):

        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="AI SIGNALS",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.box = ctk.CTkTextbox(
            self,
            width=300,
            height=220
        )

        self.box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        if signal:

            texto = f"""
Signal:
{signal['signal']}

Confidence:
{signal['confidence']} %

Trend:
{signal['trend']}

Momentum:
{signal['momentum']}

Volatility:
{signal['volatility']}
"""

            self.box.insert("1.0", texto)

            self.box.configure(state="disabled")