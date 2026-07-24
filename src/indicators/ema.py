import pandas as pd


class EMA:

    @staticmethod
    def calculate(data, period):

        return data["Close"].ewm(
            span=period,
            adjust=False
        ).mean()