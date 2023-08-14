import importlib.util
import inspect
import logging
import pkgutil
import pprint
import sys


def main():
    logging.basicConfig(level=logging.DEBUG)

    # For illustrative purposes.
    module_name = 'lphy.base'

    # found_classes = find_classes_in_module(module_name, Generator)
    found_classes = list_classes_in_package(module_name)
    pp = pprint.PrettyPrinter(indent=2)
    print(f"Loading generative distributions from {module_name} : ")
    pp.pprint(found_classes)


def get_classes_from_module(module):
    classes = []
    for cls_name, obj in inspect.getmembers(module):
        # exclude parent class
        if inspect.isclass(obj) and cls_name != 'GenerativeDistribution':
            classes.append(obj)
            logging.debug(f"class {cls_name!r} has been imported")
    return classes


def list_classes_in_package(package_name):
    package = import_module(package_name)
    class_list = get_classes_from_module(package)

    for importer, modname, ispkg in pkgutil.walk_packages(package.__path__):
        full_module_name = f"{package_name}.{modname}"
        module = import_module(full_module_name)
        class_list.extend(get_classes_from_module(module))

    return class_list


def import_module(module_name):
    if module_name in sys.modules:
        logging.warning(f"{module_name!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(module_name)) is not None:
        # If you chose to perform the actual import ...
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
