import importlib.util
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


def list_classes_in_package(package_name):
    if package_name not in sys.modules:
        package = import_module(package_name)
    else:
        package = sys.modules[package_name]
    class_list = get_classes_from_module(package)

    for loader, module_name, ispkg in pkgutil.walk_packages(package.__path__):
        # module = loader.find_module(module_name).load_module(module_name)
        full_module_name = f"{package_name}.{module_name}"
        module = import_module(full_module_name)
        class_list.extend(get_classes_from_module(module))

    return class_list


def get_classes_from_module(module):
    classes = []
    for cls_name, obj in inspect.getmembers(module):
        # TODO better way to exclude parent class?
        if inspect.isclass(obj) and cls_name != 'GenerativeDistribution':
            classes.append(obj)
            logging.debug(f"class {cls_name!r} has been imported")
    return classes


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
