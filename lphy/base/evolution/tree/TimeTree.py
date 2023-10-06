
from lphy.core.error.Errors import UnsupportedOperationException
from lphy.core.model.Function import method_info


class TimeTree:

    @method_info("the total length of the tree")
    def treeLength(self):
        pass

    @method_info("the age of the root of the tree.")
    def rootAge(self):
        pass

    @method_info("the total number of nodes in the tree (both leaf nodes and internal nodes).")
    def nodeCount(self):
        pass

    #TODO more methods

    def method_call_to_rev(self, method_name: str, args):
        if method_name == "treeLength":
            return f"treeLength()"
        elif method_name == "rootAge":
            return f"rootAge()"
        elif method_name == "nodeCount":
            return f"nnodes()"
        else:
            raise UnsupportedOperationException("")
