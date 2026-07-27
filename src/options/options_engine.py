from src.options.strike_selector import StrikeSelector
from src.options.expiration_selector import ExpirationSelector
from src.options.contracts_selector import ContractsSelector


class OptionsEngine:

    @staticmethod
    def analyze(trade, risk, timeframe="1h"):

        strike = StrikeSelector.select(trade)

        expiration = ExpirationSelector.select(timeframe)

        contracts = ContractsSelector.calculate(risk)

        return {

            "action": trade["action"],

            "confidence": trade["confidence"],

            "strike": strike,

            "expiration": expiration,

            "contracts": contracts
        }