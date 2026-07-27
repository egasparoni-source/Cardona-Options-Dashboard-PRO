from src.signals.signal_engine import SignalEngine


class SignalStep:

    @staticmethod
    def run(context):

        df = context.get("market")

        signal = SignalEngine.analyze(df)

        context.set("signal", signal)

        return context