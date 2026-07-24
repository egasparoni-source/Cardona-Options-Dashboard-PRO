import customtkinter as ctk


class RiskWidget(ctk.CTkFrame):

    def __init__(self, master, risk):

        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="RISK MANAGER",
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

        def fmt(value):
            if value is None:
                return "-"
            if isinstance(value, float):
                return round(value, 2)
            return value

        if risk:

            texto = f"""
Capital:
${fmt(risk.get("capital"))}

Risk %:
{fmt(risk.get("risk_percent"))} %

Shares:
{fmt(risk.get("shares"))}

Risk / Share:
${fmt(risk.get("risk_per_share"))}

Reward / Share:
${fmt(risk.get("reward_per_share"))}

Risk / Reward:
{fmt(risk.get("risk_reward"))}
"""

            self.box.insert("1.0", texto)
            self.box.configure(state="disabled")