from src.structure.structure_engine import StructureEngine


class StructureStep:

    @staticmethod
    def run(context):

        df = context.get("market")

        if df is None:
            return context

        structure = StructureEngine.analyze(df)

        context.set("structure", structure)

        return context