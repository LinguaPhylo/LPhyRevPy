from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value
from lphy.core.parser.UnicodeConverter import get_canonical


class ExpMarkovChain(GenerativeDistribution):

    # parameter names must be exactly same to lphy definition in @ParameterInfo
    def __init__(self, n: Value, initialMean:Value = None, firstValue:Value = None):
        super().__init__()
        self.n = n  # the dimension of the return
        self.initialMean = initialMean  # the mean of the exponential from which the first value of the chain is drawn
        self.firstValue = firstValue  # the size of the random tuple
        if (initialMean is None and firstValue is None) or (initialMean is not None and firstValue is not None):
            raise ValueError("Require either initialMean or firstValue !")
        # TODO
        if initialMean is not None:
            raise UnsupportedOperationException("The mean of the exponential parameter is not supported !")

    def sample(self, id_: str = None) -> RandomVariable:
        # not need value
        return RandomVariable(id_, None, self)

    # overwrite to F so only print the for loop, without taxa :=
    def has_var_declaration_rev(self):
        return False

    def lphy_to_rev(self, var_name):
        n = self.n.value
        loop_var = "i"

        cano_v_n = get_canonical(var_name)
        if self.firstValue is not None:
            #firstValue = self.get_param("firstValue")
            firstValue = self.firstValue.value
            # see mcmc_heterochronous_BSP.Rev
            builder = [f"{cano_v_n}[1] <- {firstValue}",  #TODO how to take theta1 to here
                       f"""for ({loop_var} in 2:{n}) {{ {cano_v_n}[{loop_var}] ~ dnExponential( 1/ {cano_v_n}[{loop_var} - 1] ) }} """]
            #TODO
            # pop_size[i].setValue(ESTIMATED_ROOT_AGE / 2)
            # moves.append(mvScale(pop_size[i], lambda =0.1, tune=true, weight=2.0))

        else: # initialMean
            raise UnsupportedOperationException("The mean of the exponential parameter is not supported !")

        return '\n'.join(builder)
