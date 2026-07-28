from src.options.strike_selector import StrikeSelector
from src.options.expiration_selector import ExpirationSelector
from src.options.contracts_selector import ContractsSelector


class OptionsEngine:

    @staticmethod
    def analyze(trade, risk, recommendation, timeframe="1h"):

        confidence = recommendation["confidence"]

        strike = StrikeSelector.select(confidence)

        expiration = ExpirationSelector.select(timeframe)

        contracts = ContractsSelector.calculate(risk)

        return {

            "action": recommendation["action"],

            "confidence": confidence,

            "strike": strike,

            "expiration": expiration,

            "contracts": contracts
        }