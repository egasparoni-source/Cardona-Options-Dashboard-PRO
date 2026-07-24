class BaseStrategy:

    name = "Base Strategy"

    @staticmethod
    def analyze(data):
        raise NotImplementedError