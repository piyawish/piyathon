# Development

## Prompts

The prompt for generating documentation of a file:

Generate detailed code documentation for [filename] using standardized comments that describe:

* File purpose and core functionality
* Key dependencies and imports
* Data structures and their relationships
* Functions/methods with:
  * Input parameters and expected types
  * Return values and types
  * Side effects or state changes
  * Usage examples
* Known limitations or edge cases
* Integration points with other system components
* Any complex algorithms or business logic

Use the appropriate documentation format for the programming language (e.g., JSDoc for JavaScript, docstrings for Python). Structure the comments hierarchically from high-level overview to specific implementation details. Include code examples where they add clarity.

For Python files, place the documentation as a module docstring (triple quotes) immediately after any copyright notice and before import statements. For other languages, ensure the documentation is not placed above any copyright notice if it exists.
