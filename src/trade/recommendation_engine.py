class RecommendationEngine:

    @staticmethod
    def analyze(setup):

        if setup is None:
            return None

        score = setup["score"]

        trend = setup["trend"]

        rr = setup["risk_reward"]

        if (
            score >= 90
            and trend == "STRONG_BULL"
            and rr >= 2
        ):

            action = "BUY CALL"

            confidence = 95

        elif (
            score >= 80
            and rr >= 2
        ):

            action = "BUY CALL"

            confidence = 85

        elif score <= 20:

            action = "BUY PUT"

            confidence = 80

        else:

            action = "WAIT"

            confidence = 50

        return {

            "action": action,

            "confidence": confidence
        }