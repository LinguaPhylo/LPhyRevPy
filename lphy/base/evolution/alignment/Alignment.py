from lphy.core.error.Errors import UnsupportedOperationException


class Alignment():

    def method_call_to_rev(self, method_name: str, args):
        if method_name == "nchar":
            return f"nchar()"
        elif method_name == "taxa":
            return f"taxa()"
        elif method_name == "taxaNames": # Rev taxa has no names()
            return f"names()"
        else:
            raise UnsupportedOperationException()


#TODO

# map of method call to rev method

# map = {"taxa()" : "taxa()"}

# @MethodInfo(description = "the taxa of the alignment."
# what about agrs?
