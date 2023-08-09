from lphy.core.graphicalmodel.Generator import Generator


class GenerativeDistribution(Generator):

    def specification_operator(self):
        return '~'
