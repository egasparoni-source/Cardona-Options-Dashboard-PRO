from src.trade.recommendation_engine import RecommendationEngine


class RecommendationStep:

    @staticmethod
    def run(context):

        trade = context.get("trade")

        if trade is None:
            return context

        recommendation = RecommendationEngine.analyze(trade)

        context.set("recommendation", recommendation)

        return context