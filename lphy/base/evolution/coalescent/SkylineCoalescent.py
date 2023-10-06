from lphy.core.model.GenerativeDistribution import GenerativeDistribution
from lphy.core.parser.RevBuilder import get_argument_rev_string
from lphy.core.model.RandomVariable import RandomVariable
from lphy.core.model.Value import Value
from lphy.core.error.Errors import UnsupportedOperationException


class SkylineCoalescent(GenerativeDistribution):
#TODO
    def __init__(self, theta: Value, groupSizes:Value = None, n: Value = None, taxa: Value = None, ages: Value = None):
        super().__init__()
        self.theta = theta
        self.groupSizes = groupSizes
        self.n = n
        self.taxa = taxa
        self.ages = ages

        c = (0 if ages is None else 1) + (0 if taxa is None else 1) + (0 if n is None else 1)
        if c > 1:
            raise ValueError("Only one of 'n' or 'taxa' or 'ages' should be provided to 'SkylineCoalescent' !")

    def sample(self, id_: str = None) -> RandomVariable:
        # must return a TimeTree obj, otherwise it cannot convert the method calls
        from lphy.base.evolution.tree.TimeTree import TimeTree
        return RandomVariable(id_, TimeTree(), self)

    def lphy_to_rev(self, var_name):
        # lphy names are same to rev
        theta_name = "theta"
        taxa_name = "taxa"
        theta = self.get_param(theta_name)
        if self.taxa is not None:
            taxa = self.get_param(taxa_name)
        elif self.n is not None:
            n = self.n.value
            #TODO taxa =, cannot create Rev code to create taxa in this stage
            raise UnsupportedOperationException("TODO !")
        elif self.ages is not None:
            ages = self.ages.value
            # TODO taxa =
            raise UnsupportedOperationException("TODO !")
        else:
            raise UnsupportedOperationException("SkylineCoalescent conversion requires taxa currently !")

        # https://revbayes.github.io/tutorials/coalescent/skyline
        # dnCoalescentSkyline(theta=pop_size, method="events", events_per_interval=final_number_events_pi, taxa=taxa)
        builder = [f"""{get_argument_rev_string(theta_name, theta)}""", 'method="events"']
        if self.groupSizes is not None:
            group_sizes = self.get_param("groupSizes")
            # TODO what is "times" comparing to the old param "events_per_interval"
            builder.append(f"""{get_argument_rev_string("times", group_sizes)}""")
        else:
            # By default, all group sizes are 1 which is equivalent to the classic skyline coalescent.
            theta_val = theta.value
            if not isinstance(theta_val, list) or len(theta_val) < 3:
                raise RuntimeError(f"The number of population sizes ({len(theta_val)}) is incorrect in 'SkylineCoalescent' !")
            group_sizes = [1] * (len(theta_val) - 1)
            # TODO what is "times" comparing to the old param "events_per_interval"
            builder.append(f"""times={group_sizes}""")

        builder.append(f"""{get_argument_rev_string(taxa_name, taxa)}""")
        args = ", ".join(builder)
        return f"dnCoalescentSkyline({args})"
