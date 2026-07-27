class ContractsSelector:

    @staticmethod
    def calculate(risk):

        capital = risk["capital"]

        if capital < 5000:
            return 1

        elif capital < 15000:
            return 2

        elif capital < 30000:
            return 3

        return 5