from src.indicators.ema import EMA
from src.indicators.rsi import RSI
from src.indicators.macd import MACD
from src.indicators.vwap import VWAP
from src.indicators.atr import ATR


class IndicatorEngine:

    @staticmethod
    def calculate(df):
        """
        Calcula todos los indicadores técnicos y los agrega
        al DataFrame recibido.
        """

        if df is None or df.empty:
            return df

         # Medias para Intradía
        df["EMA20"] = EMA.calculate(df, 20)
        df["EMA40"] = EMA.calculate(df, 40)
        df["EMA100"] = EMA.calculate(df, 100)
        df["EMA200"] = EMA.calculate(df, 200)

         # Medias Cardona
        df["EMA40"] = EMA.calculate(df, 40)
        df["EMA100"] = EMA.calculate(df, 100)
        df["EMA200"] = EMA.calculate(df, 200)
        # RSI
        df["RSI"] = RSI.calculate(df)

        # VWAP
        df["VWAP"] = VWAP.calculate(df)

        # ATR
        df["ATR"] = ATR.calculate(df)

        # MACD
        macd, signal, hist = MACD.calculate(df)

        df["MACD"] = macd
        df["MACD_SIGNAL"] = signal
        df["MACD_HIST"] = hist

        return df