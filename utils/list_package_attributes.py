# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import importlib
import inspect
import sys


def list_package_attributes(package_name):
    try:
        # Dynamically import the package
        package = importlib.import_module(package_name)
    except ImportError:
        print(f"Package '{package_name}' not found.")
        return

    # Get all public attributes of the package
    attributes = [attr for attr in dir(package) if not attr.startswith("_")]

    # Filter classes
    classes = [attr for attr in attributes if inspect.isclass(getattr(package, attr))]

    # Filter methods
    methods = [attr for attr in attributes if inspect.ismethod(getattr(package, attr))]

    # Filter functions
    functions = [
        attr for attr in attributes if inspect.isfunction(getattr(package, attr))
    ]

    # Filter constants (assuming constants are uppercase)
    constants = [attr for attr in attributes if attr.isupper()]

    if len(classes) > 0:
        print(f"\nClasses in {package_name} package:")
        for cls in classes:
            print(f"  {cls}")

    if len(methods) > 0:
        print(f"\nMethods in {package_name} package:")
        for mtd in methods:
            print(f"  {mtd}")

    if len(functions) > 0:
        print(f"\nFunctions in {package_name} package:")
        for func in functions:
            print(f"  {func}")

    if len(constants) > 0:
        print(f"\nConstants in {package_name} package:")
        for const in constants:
            print(f"  {const}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python list_package_attributes.py <package_name>")
    else:
        package_name = sys.argv[1]
        list_package_attributes(package_name)
