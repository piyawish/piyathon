# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Piyathon Package Initialization Module

This module initializes the Piyathon package and sets up the runtime environment.
It handles dynamic module loading from the Lib directory and exports package metadata.

Core Functionality:
    - Dynamically imports all modules from the Lib package
    - Exports package version information
    - Manages package-level exports via __all__

Dependencies:
    - importlib: For dynamic module importing
    - pkgutil: For module discovery and iteration

Integration Points:
    - Interfaces with the Lib directory for standard library modules
    - Provides version information to the CLI and other components
    - Controls package-level symbol visibility

Side Effects:
    - Modifies the module namespace with imported symbols
    - Populates __all__ with all local symbols
"""

import importlib
import pkgutil

# Import all modules in the .Lib package dynamically
package_name = "Lib"

for _, module_name, _ in pkgutil.iter_modules([package_name]):
    importlib.import_module(f".{module_name}", package=package_name)

__all__ = list(locals())

__version__ = "0.3.12.11"
