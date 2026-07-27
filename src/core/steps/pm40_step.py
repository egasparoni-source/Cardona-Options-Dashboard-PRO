from src.strategy.pm40 import PM40Strategy


class PM40Step:

    @staticmethod
    def run(context):

        df = context.get("market")
        mtf = context.get("mtf")

        if df is None or mtf is None:
            return context

        pm40 = PM40Strategy.analyze(df, mtf)

        context.set("pm40", pm40)

        return context