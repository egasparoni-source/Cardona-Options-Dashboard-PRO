import pandas as pd


class ATR:

    @staticmethod
    def calculate(data, period=14):
        """
        Calcula el Average True Range (ATR).
        """

        high_low = data["High"] - data["Low"]

        high_close = (data["High"] - data["Close"].shift()).abs()

        low_close = (data["Low"] - data["Close"].shift()).abs()

        true_range = pd.concat(
            [high_low, high_close, low_close],
            axis=1
        ).max(axis=1)

        atr = true_range.rolling(period).mean()

        return atr