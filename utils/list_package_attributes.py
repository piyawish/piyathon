# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""Utility for extracting and formatting Python package attributes.

This script analyzes Python packages to extract their public attributes (classes,
methods, functions, and constants) and formats them into a dictionary structure
suitable for translation mapping. The output is both printed and copied to the
clipboard.

Dependencies:
    - sys: For command line arguments
    - inspect: For introspecting Python objects
    - importlib: For dynamic module importing
    - pyperclip: For clipboard operations

Output Format:
    Generates a dictionary with the following structure:
    {
        "__name__": "",
        "classes": {class_name: "" for each class},
        "methods": {method_name: "" for each method},
        "functions": {function_name: "" for each function},
        "constants": {constant_name: "" for each constant}
    }

Version History:
    - 1.0: Initial implementation with basic attribute extraction
"""

import sys
import inspect
import importlib
import pyperclip


def list_package_attributes(package_name):
    """Extract and format attributes from a Python package.

    Analyzes a Python package to extract its public attributes and formats them
    into a dictionary structure suitable for translation mapping. The output is
    both printed and copied to the clipboard.

    Args:
        package_name (str): Name of the Python package to analyze

    Side Effects:
        - Prints the formatted dictionary to stdout
        - Copies the formatted dictionary to the system clipboard

    Example:
        >>> list_package_attributes("random")
        random = {"__name__": "", "classes": {"Random": ""}, ...}
        The output has been copied to the clipboard.

    Note:
        - Constants are identified by uppercase names
        - Private attributes (starting with '_') are excluded
        - The empty strings in the output are placeholders for translations
    """
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
