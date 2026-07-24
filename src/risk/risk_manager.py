from src.risk.position_size import PositionSize


class RiskManager:

    @staticmethod
    def analyze(
        capital,
        risk_percent,
        entry,
        stop,
        target
    ):

        shares = PositionSize.calculate(
            capital,
            risk_percent,
            entry,
            stop
        )

        risk = abs(entry - stop)

        reward = abs(target - entry)

        rr = round(reward / risk, 2) if risk > 0 else 0

        return {

            "capital": capital,

            "risk_percent": risk_percent,

            "shares": shares,

            "risk_per_share": round(risk, 2),

            "reward_per_share": round(reward, 2),

            "risk_reward": rr
        }