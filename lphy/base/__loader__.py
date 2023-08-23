import importlib
import inspect
import logging
import pkgutil
import pprint
import sys


# TODO have to add __init__, pkgutil.walk_packages cannot search children pkgs recursively in non-module
MODULE_NAME = 'lphy.base'

# TODO why __loader__ has to be under lphy.base?
def main():
    logging.basicConfig(level=logging.DEBUG)

    # found_classes = find_classes_in_module(module_name, Generator)
    found_classes = list_classes_in_package(MODULE_NAME)
    pp = pprint.PrettyPrinter(indent=2)
    print(f"Loading generative distributions from {MODULE_NAME} : ")
    pp.pprint(found_classes)

    # Get the constructor of LogNormal
    constructor = found_classes[0].__init__

    # Get the parameters of the constructor
    parameters = inspect.signature(constructor).parameters

    # Print the parameters and their default values
    for param_name, param in parameters.items():
        print(f"Parameter: {param_name}, Default Value: {param.default}")


def list_classes_in_package(module_name):
    # if module_name not in sys.modules:
    #     module = importlib.import_module(module_name)
    # else:
    #     module = sys.modules[module_name]

    module = importlib.import_module(module_name)
#    class_list = get_classes_from_module(module)
    class_list = []

    for _, submodule_name, _ in pkgutil.walk_packages(module.__path__, module_name + '.'):
        # module = loader.find_module(module_name).load_module(module_name)
        #full_module_name = f"{module_name}.{module_name}"
        submodule = importlib.import_module(submodule_name)
        #submodule_classes = get_classes_from_module(submodule)
        # TODO better way to exclude parent class?
        submodule_classes = [obj for obj in vars(submodule).values() if isinstance(obj, type)]
        class_list.extend(submodule_classes)

    return class_list


# def get_classes_from_module(module):
#     classes = []
#     for cls_name, obj in vars(module):
#         # TODO better way to exclude parent class?
#         if inspect.isclass(obj) and cls_name != 'GenerativeDistribution':
#             classes.append(obj)
#             logging.debug(f"class {cls_name!r} has been imported")
#     return classes


def import_module(module_name):
    if module_name in sys.modules:
        logging.warning(f"{module_name!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(module_name)) is not None:
        # perform the actual import
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        if is_module(module_name):
            logging.debug(f"module {module_name!r} has been imported")
        return module
    else:
        logging.error(f"can't find the {module_name!r} module")


def is_module(name):
    try:
        module = __import__(name)
        return inspect.ismodule(module)
    except ImportError:
        return False


if __name__ == "__main__":
    main()
