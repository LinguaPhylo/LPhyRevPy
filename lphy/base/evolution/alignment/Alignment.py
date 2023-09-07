from typing import List

from lphy.base.evolution.taxa.Taxa import Taxa, Taxon
from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import method_info


class Alignment(Taxa):

    @method_info("The number of characters/sites.")
    def nchar(self):
        pass

    @method_info("the taxa of the alignment.")
    def taxa(self):
        return Taxa()

    def method_call_to_rev(self, method_name: str, args):
        if method_name == "nchar":
            return f"nchar()"
        elif method_name == "taxa":
            return f"taxa()"
        elif method_name == "taxaNames":  # Rev taxa has no names()
            return f"names()"
        else:
            raise UnsupportedOperationException("")

# TODO

# map of method call to rev method

# map = {"taxa()" : "taxa()"}

# @MethodInfo(description = "the taxa of the alignment."
# what about agrs?
