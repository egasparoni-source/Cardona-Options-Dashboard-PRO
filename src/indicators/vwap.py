class VWAP:

    @staticmethod
    def calculate(data):
        """
        Calcula el Volume Weighted Average Price (VWAP).
        """

        typical_price = (
            data["High"] +
            data["Low"] +
            data["Close"]
        ) / 3

        vwap = (
            (typical_price * data["Volume"]).cumsum()
            / data["Volume"].cumsum()
        )

        return vwap