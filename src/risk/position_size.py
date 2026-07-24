class PositionSize:

    @staticmethod
    def calculate(
        capital,
        risk_percent,
        entry,
        stop
    ):
        """
        Calcula el tamaño de posición.

        capital = dinero disponible
        risk_percent = porcentaje a arriesgar (1 = 1%)
        """

        risk_amount = capital * (risk_percent / 100)

        risk_per_share = abs(entry - stop)

        if risk_per_share == 0:
            return 0

        shares = risk_amount / risk_per_share

        return int(shares)