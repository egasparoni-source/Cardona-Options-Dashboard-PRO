class MACD:

    @staticmethod
    def calculate(data, fast=12, slow=26, signal=9):
        """
        Calcula MACD, Signal y Histogram.
        """

        ema_fast = data["Close"].ewm(span=fast, adjust=False).mean()
        ema_slow = data["Close"].ewm(span=slow, adjust=False).mean()

        macd = ema_fast - ema_slow

        signal_line = macd.ewm(span=signal, adjust=False).mean()

        histogram = macd - signal_line

        return macd, signal_line, histogram