from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value


class Coalescent(GenerativeDistribution):

    def __init__(self, theta: Value, n: Value = None, taxa: Value = None):
        # this is more restrict, to avoid requiring extra Rev code to create taxa
        if (n is not None and taxa is not None) or (n is None and taxa is None):
            raise ValueError("Either 'n' or 'taxa' should be provided to 'Coalescent', but not both or neither !")

        super().__init__()
        self.theta = theta
        self.n = n
        self.taxa = taxa

    def sample(self, id_: str = None) -> RandomVariable:
        # must return a TimeTree obj, otherwise it cannot convert the method calls
        from lphy.base.evolution.tree.TimeTree import TimeTree
        return RandomVariable(id_, TimeTree(), self)

    # TODO https://revbayes.github.io/documentation/dnHeterochronousCoalescent.html
    def lphy_to_rev(self, var_name):
        # lphy names are same to rev
        theta_name = "theta"
        taxa_name = "taxa"
        theta = self.get_param(theta_name)

        builder = [get_argument_rev_string(theta_name, theta)]

        if self.taxa is not None:
            taxa = self.get_param(taxa_name)
            builder.append(get_argument_rev_string(taxa_name, taxa))
        elif self.n is not None:
            # here must be same as def rev_code_before(self, var_name):
            taxa_var_name = var_name + "_taxa"
            builder.append(f"taxa={taxa_var_name}")
        else:
            raise ValueError("Either 'n' or 'taxa' should be provided to 'Coalescent', but not both or neither !")

        args = ", ".join(builder)
        return f"dnCoalescent({args})"

    def rev_code_before(self, var_name):
        if self.n is not None:
            n = self.n.value
            from lphy.base.evolution.taxa.Taxa import create_n_taxa
            return create_n_taxa(n, var_name)
        else:
            pass
