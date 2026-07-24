import customtkinter as ctk


class PM40Widget(ctk.CTkFrame):

    def __init__(self, master, pm40):

        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="PM40 STRATEGY",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        self.box = ctk.CTkTextbox(
            self,
            width=300,
            height=350
        )

        self.box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        def fmt(value):
            if value is None:
                return "-"
            if isinstance(value, (int, float)):
                return f"{value:.2f}"
            return str(value)

        if pm40:

            texto = f"""Signal:
{pm40.get("signal", "-")}

Score:
{pm40.get("score", "-")}

Entry:
{fmt(pm40.get("entry"))}

Stop:
{fmt(pm40.get("stop"))}

Target 1:
{fmt(pm40.get("target1"))}

Target 2:
{fmt(pm40.get("target2"))}

Risk / Reward:
{pm40.get("risk_reward", "-")}
"""

            self.box.insert("1.0", texto)
            self.box.configure(state="disabled")