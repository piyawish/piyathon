# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Unit Tests for Piyathon CLI Module

This module contains unit tests for the Piyathon command-line interface functionality.
It tests various error conditions and edge cases for file handling and argument parsing.

Test Coverage:
    - Command-line argument validation
    - File extension validation
    - File existence and readability checks
    - Error message formatting and content

Dependencies:
    - pytest: For test framework and fixtures
    - unittest.mock: For mocking system calls and file operations
    - sys: For command-line argument manipulation
"""

import sys
from unittest.mock import patch, mock_open
import pytest
from piyathon.piyathon import main


def test_no_arguments(capsys):
    """
    Test behavior when no command-line arguments are provided.

    This test verifies that the CLI properly handles the case when no source file
    is specified, ensuring it exits with the correct error code and message.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 2
        - Error message indicates missing required argument
    """
    test_args = ["piyathon.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 2
        captured = capsys.readouterr()
        assert "required" in captured.err


def test_invalid_extension(capsys):
    """
    Test behavior when a file with an invalid extension is provided.

    This test ensures that the CLI properly validates file extensions,
    requiring .pi files and rejecting other extensions.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 1
        - Error message indicates invalid file extension
    """
    test_args = ["piyathon.py", "source.txt"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert "Error: The source file must have a .pi extension" in captured.out


def test_file_not_found(capsys):
    """
    Test behavior when the specified source file does not exist.

    This test verifies that the CLI properly handles non-existent input files,
    providing appropriate error messages and exit codes.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 1
        - Error message indicates file not found
    """
    test_args = ["piyathon.py", "nonexistent.pi"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert "Error: Input file 'nonexistent.pi' not found." in captured.out


def test_file_read_error(capsys):
    """
    Test behavior when the source file cannot be read.

    This test ensures that the CLI properly handles I/O errors when reading
    the source file, providing appropriate error messages and exit codes.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 1
        - Error message indicates file read error
    """
    test_args = ["piyathon.py", "source.pi"]
    with patch.object(sys, "argv", test_args):
        with patch("builtins.open", mock_open()) as mocked_open:
            mocked_open.side_effect = IOError
            with pytest.raises(SystemExit) as e:
                main()
            assert e.type == SystemExit
            assert e.value.code == 1
            captured = capsys.readouterr()
            assert "Error: Unable to read input file 'source.pi'." in captured.out
