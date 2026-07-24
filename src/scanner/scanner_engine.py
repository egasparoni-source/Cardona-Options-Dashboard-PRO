from src.controller.dashboard_controller import DashboardController


class ScannerEngine:

    SYMBOLS = [
        "SPY",
        "QQQ",
        "AAPL",
        "MSFT",
        "NVDA",
        "META",
        "AMD",
        "TSLA",
        "AMZN",
        "GOOGL"
    ]

    @staticmethod
    def scan():

        results = []

        for symbol in ScannerEngine.SYMBOLS:

            try:

                dashboard = DashboardController.load(symbol)

                if dashboard is None:
                    continue

                pm40 = dashboard["pm40"]

                results.append({
                    "symbol": symbol,
                    "signal": pm40["signal"],
                    "score": int(pm40["score"]),
                    "entry": float(round(pm40["entry"], 2)),
                    "rr": float(pm40["risk_reward"])
                })

            except Exception:
                continue

        results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return results