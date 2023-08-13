from lphy.core.model.Generator import Generator


class ParserUtils:
    MAX_UNNAMED_ARGS = 3
    REPLICATES_PARAM_NAME = "replicates"  # Replace with the actual parameter name
#TODO
    @staticmethod
    def get_matching_functions(name, arg_values):
        matches = []
        for function_class in LoaderManager.get_function_classes(name):
            matches.extend(ParserUtils._get_function_by_arguments(name, arg_values, function_class))
        return matches

    @staticmethod
    def get_matching_generative_distributions(name, arguments) -> [Generator]:
        matches = []

        generators = LoaderManager.get_all_generative_distribution_classes(name)

        if generators is not None:
            for gen_class in generators:
                matches.extend(ParserUtils._get_generator_by_arguments(name, arguments, gen_class))
        else:
            raise RuntimeError(f"No generator with name {name} available.")
        return matches

    ### private

    @staticmethod
    def _get_generator_by_arguments(name, arguments, generator_class):
        matches = []

        for constructor in generator_class.__constructors__:
            argument_info = ArgumentUtils.get_arguments(constructor)
            initargs = []

            if ParserUtils._match(arguments, argument_info):

                for i in range(len(argument_info)):
                    arg = arguments.get(argument_info[i].name)
                    if arg is not None:
                        initargs.append(arg)
                    elif not argument_info[i].optional:
                        raise RuntimeError(f"Required argument {argument_info[i].name} not found!")
                    else:
                        initargs.append(None)

                matches.append(ParserUtils._construct_generator(name, constructor, argument_info, initargs, arguments, False))
        return matches

    @staticmethod
    def _match(arguments, argument_info):
        required_arguments = set()
        optional_arguments = set()
        keys = set(arguments.keys())

        for argument_inf in argument_info:
            if argument_inf.optional:
                optional_arguments.add(argument_inf.name)
            else:
                required_arguments.add(argument_inf.name)

        if not keys.issuperset(required_arguments):
            return False

        keys.difference_update(required_arguments)
        keys.difference_update(optional_arguments)
        return len(keys) == 0 or (len(keys) == 1 and ParserUtils.REPLICATES_PARAM_NAME in keys)

    @staticmethod
    def _get_function_by_arguments(name, arg_values, generator_class):
        matches = []
        for constructor in generator_class.__constructors__:
            arguments = ArgumentUtils.get_arguments(constructor)

            if len(arg_values) == len(arguments) and 0 < len(arg_values) <= ParserUtils.MAX_UNNAMED_ARGS:
                f = ParserUtils._construct_generator(name, constructor, arguments, arg_values, None, False)
                if f is not None:
                    matches.append(f)
            elif len(arg_values) == 0 and all(x.optional for x in arguments):
                f = ParserUtils._construct_generator(name, constructor, arguments, [None] * len(arguments), None, False)
                if f is not None:
                    matches.append(f)
        return matches

    @staticmethod
    def _construct_generator(name, constructor, arguments, initargs, params, lightweight):
        if ArgumentUtils.matching_parameter_types(arguments, initargs, params, lightweight):
            return constructor(*initargs)
        elif IID.match(constructor, arguments, initargs, params):
            iid = IID(constructor, initargs, params)
            if iid.size() == 1:
                return constructor(*initargs)
            return iid
        elif VectorMatchUtils.vector_match(arguments, initargs) > 0:
            return VectorMatchUtils.vector_generator(constructor, arguments, initargs)
        else:
            raise RuntimeError(f"ERROR! No match in '{name}' constructor arguments, including vector match! ")

