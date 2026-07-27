class StrikeSelector:

    @staticmethod
    def select(trade):

        confidence = trade["confidence"]

        if confidence >= 90:
            return "ATM"

        elif confidence >= 75:
            return "ITM"

        return "OTM"