class ExpirationSelector:

    @staticmethod
    def select(timeframe):

        mapping = {

            "5m": "7 DTE",

            "15m": "14 DTE",

            "1h": "21 DTE",

            "1d": "45 DTE",

            "1wk": "90 DTE",

            "1mo": "180 DTE"

        }

        return mapping.get(timeframe, "21 DTE")