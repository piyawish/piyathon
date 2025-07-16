# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Piyathon is a Thai language-localized superset of Python that uses Thai keywords and function names. The project employs a sophisticated translation approach combining tokenization and Abstract Syntax Tree (AST) manipulation to convert between standard Python and Piyathon code.

## Core Architecture

### Main Components

- **piyathon/piyathon_translator.py** - Core translation engine that converts between Python and Piyathon using AST manipulation
- **piyathon/piyathon.py** - Main CLI entry point and runtime environment for executing .pi files
- **piyathon/p2p.py** - Bidirectional translation tool between .py and .pi files
- **piyathon/keywords.py** - Defines keyword mappings and translations between Python and Piyathon
- **piyathon/Lib/** - Contains Thai translations of Python standard library modules (สุ่ม.py for random, เต่า.py for turtle)

### File Extensions

- `.pi` files contain Piyathon source code
- `.py` files contain standard Python code
- The translator converts bidirectionally between these formats

## Development Commands

### Setup

```bash
uv sync                      # Install dependencies and create virtual environment
uv add --dev <package>       # Add development dependency
uv remove <package>          # Remove dependency
```

### Testing

```bash
make test                    # Run full test suite (includes CPython file tests)
uv run pytest tests         # Run pytest directly
uv run pytest tests/test_*.py  # Run specific test files
```

### Building and Distribution

```bash
make build                   # Build package using uv
uv build                     # Direct uv build command
make clean                   # Clean build artifacts
make upload                  # Upload to PyPI (after build and check)
make test-upload             # Upload to test PyPI
```

### Documentation

```bash
cd docs && make html         # Build Sphinx documentation
cd docs && make livehtml     # Live rebuild documentation server
cd docs && make upload_all   # Upload docs to Google Cloud Storage
cd docs && make validate     # Validate HTML output
```

### Usage Examples

```bash
uv run piyathon example.pi   # Execute Piyathon file
uv run p2p input.py output.pi  # Convert Python to Piyathon
uv run p2p input.pi output.py  # Convert Piyathon to Python
```

## Code Translation Process

The translation process involves:

1. Tokenizing source code
2. Generating Abstract Syntax Tree (AST)
3. Transforming AST by translating Thai keywords/functions to English equivalents (or vice versa)
4. Generating code in target language

This ensures full compatibility with Python's syntax and features while providing a Thai language interface.

## Testing Strategy

- **tests/test_cpython_files.py** - Tests Python to Piyathon translation on real CPython files
- **tests/test_examples.py** - Tests example programs and core functionality
- **tests/piyathon/** - Contains unit tests for individual modules
- Tests require a CPython repository at `../cpython` for comprehensive translation testing

## Dependencies

- Requires Python 3.12+
- Uses uv for dependency management and building
- Uses hatchling as build backend
- Development dependencies managed via uv (pytest, twine, sphinx, etc.)
- No runtime dependencies (uses only Python standard library)

## Thai Language Integration

- Thai characters are supported in variable names, function names, and comments
- Built-in functions, constants, and error messages are translated to Thai
- Standard library modules have Thai equivalents in piyathon/Lib/
- Full bidirectional translation preserves code semantics while changing language interface

## Git Commit Guidelines

- Do not include Claude Code signature or attribution in commit messages
- Keep commit messages clean and focused on the actual changes made
