# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import importlib
import pkgutil

# Import all modules in the .Lib package dynamically
package_name = "Lib"

for _, module_name, _ in pkgutil.iter_modules([package_name]):
    importlib.import_module(f".{module_name}", package=package_name)

__all__ = list(locals())

__version__ = "0.3.12.7"
