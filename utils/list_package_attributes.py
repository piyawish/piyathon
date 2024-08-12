# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import sys
import inspect
import importlib
import pyperclip


def list_package_attributes(package_name):
    try:
        package = importlib.import_module(package_name)
    except ImportError:
        print(f"Error: Package '{package_name}' not found.")
        return

    attributes = dir(package)

    # Filter and sort classes
    classes = sorted(
        [attr for attr in attributes if inspect.isclass(getattr(package, attr))]
    )

    # Filter and sort methods
    methods = sorted(
        [attr for attr in attributes if inspect.ismethod(getattr(package, attr))]
    )

    # Filter and sort functions
    functions = sorted(
        [attr for attr in attributes if inspect.isfunction(getattr(package, attr))]
    )

    # Filter and sort constants (assuming constants are uppercase)
    constants = sorted([attr for attr in attributes if attr.isupper()])

    library_dict = {
        "__name__": "",
        "classes": {cls: "" for cls in classes},
        "methods": {mtd: "" for mtd in methods},
        "functions": {func: "" for func in functions},
        "constants": {const: "" for const in constants},
    }

    output = f"{package_name} = {library_dict}"
    print(output)
    pyperclip.copy(output)
    print("\nThe output has been copied to the clipboard.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python list_package_attributes.py <package_name>")
    else:
        package_name = sys.argv[1]
        list_package_attributes(package_name)
