from src.strategy.pm40 import PM40Strategy


class StrategyEngine:

    @staticmethod
    def analyze(df, mtf):

        strategies = []

        strategies.append(
            PM40Strategy.analyze(df, mtf)
        )

        return strategies