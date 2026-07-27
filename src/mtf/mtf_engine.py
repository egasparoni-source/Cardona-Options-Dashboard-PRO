from src.mtf.timeframe_analyzer import TimeframeAnalyzer
from src.mtf.score_engine import ScoreEngine


class MTFEngine:

    TIMEFRAMES = {
        "1H": "1h",
        "1D": "1d",
        "1W": "1wk",
        "1M": "1mo"
    }

    @staticmethod
    def analyze(symbol):

        result = {}

        total = 0

        for name, interval in MTFEngine.TIMEFRAMES.items():

            analysis = TimeframeAnalyzer.analyze(
                symbol,
                interval
            )

            if analysis is None:
                continue

            analysis.update(
                ScoreEngine.calculate(analysis)
            )

            result[name] = analysis

            total += analysis["score"]

        if result:

            result["GLOBAL"] = round(
                total / len(result),
                1
            )

        return result