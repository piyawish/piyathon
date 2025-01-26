# Development

## Folder Structure

### /piyathon

Core package directory containing the main implementation files:

- `__init__.py` - Package initialization and version information
- `piyathon.py` - Main entry point and runtime environment for executing Piyathon code
- `piyathon_translator.py` - Core translation engine for converting between Python and Piyathon code
- `p2p.py` - Command-line tool for bidirectional translation between .py and .pi files
- `keywords.py` - Defines keyword mappings and translations between Python and Piyathon
- `Lib/` - Directory containing translated standard library modules

### /tests

Test suite directory:

- `__init__.py` - Test package initialization
- `conftest.py` - PyTest configuration and shared test fixtures
- `test_cpython_files.py` - Tests for Python to Piyathon code translation
- `test_examples.py` - Tests for example Piyathon programs and functionality
- `piyathon/` - Directory containing test files and resources

## Development Files

### Main Project Files

- `README.md` - Primary documentation with project overview, installation instructions, and usage examples
- `DEVELOPMENT.md` - Development guidelines and documentation for contributors
- `NOTES.md` - Additional development notes and documentation
- `LICENSE` - Project's legal license terms

### Core Code Directories

- `piyathon/` - Main package directory with core implementation files
- `tests/` - Test suite directory containing all project tests
- `examples/` - Example code demonstrating project usage
- `utils/` - Helper scripts and utilities for development tasks
- `docs/` - Project documentation and configuration

### Project Configuration

- `pyproject.toml` - Python project configuration and build settings
- `requirements.in` - Direct project dependencies (source file)
- `requirements.txt` - Complete list of all dependencies with pinned versions
- `.pylintrc` - Python code linting configuration
- `Makefile` - Commands for common development tasks
- `.gitignore` - Specifies which files Git should ignore

### Build and Environment

- `dist/` - Contains built distribution packages (generated)
- `venv/` - Python virtual environment (local development)
- `tmp/` - Temporary files directory
- `.pytest_cache/` - Cache directory for pytest

### IDE Configuration

- `piyathon.code-workspace` - VS Code workspace settings
- `git-view.code-workspace` - Additional VS Code workspace configuration

### Development Workflow

1. Start by reading `README.md` for project overview
2. Set up development environment following instructions in this document
3. Create a virtual environment and install dependencies from `requirements.txt`
4. Explore example code in `examples/` directory
5. Use `Makefile` commands for common development tasks
6. Write tests in `tests/` directory for new features
7. Follow existing project structure in `piyathon/` when adding code
8. Use utilities in `utils/` directory as needed during development
