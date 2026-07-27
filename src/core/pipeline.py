class Pipeline:

    def __init__(self):

        self.steps = []

    def add(self, func):

        self.steps.append(func)

    def run(self, context):

        for step in self.steps:

            context = step(context)

        return context