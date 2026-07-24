import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import mplfinance as mpf

from src.market.market_data import MarketData
from src.indicators.indicator_engine import IndicatorEngine


class ChartWidget(ctk.CTkFrame):

    def __init__(self, master, symbol="SPY"):
        super().__init__(master)

        self.symbol = symbol

        # Crear figura
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # Dibujar gráfico inicial
        self.load_chart(self.symbol)

    def load_chart(self, symbol):
        self.symbol = symbol

        datos = MarketData.get_price(symbol)

        if datos is None or datos.empty:
            return

        # Calcular indicadores
        datos = IndicatorEngine.calculate(datos)

        # Mostrar solo las últimas 200 velas
        datos = datos.tail(200)

        self.ax.clear()

        # EMAs
        apds = [
            mpf.make_addplot(datos["EMA20"], ax=self.ax),
            mpf.make_addplot(datos["EMA40"], ax=self.ax),
            mpf.make_addplot(datos["EMA100"], ax=self.ax),
            mpf.make_addplot(datos["EMA200"], ax=self.ax),
        ]

        # Plot
        mpf.plot(
            datos,
            type="candle",
            ax=self.ax,
            addplot=apds,
            style="charles",
            volume=False,
            warn_too_much_data=1000
        )

        self.ax.set_title(f"{symbol} - Candlestick")

        self.canvas.draw()