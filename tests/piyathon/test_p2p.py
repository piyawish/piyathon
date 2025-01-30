# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

"""
Unit Tests for Piyathon-Python Translation Tool

This module contains unit tests for the command-line tool that translates
between Piyathon (.pi) and Python (.py) source files. It verifies file handling,
error conditions, and bidirectional translation functionality.

Test Coverage:
    - Command-line argument validation
    - File extension validation
    - File existence and readability checks
    - Error message formatting
    - Bidirectional translation integrity
    - File I/O operations

Dependencies:
    - pytest: For test framework and fixtures
    - unittest.mock: For mocking system calls and file operations
    - sys: For command-line argument manipulation
    - tmp_path: For temporary file creation and cleanup
"""

import sys
from unittest.mock import patch, mock_open
import pytest
from piyathon.p2p import main


def test_wrong_number_of_arguments(capsys):
    """
    Test behavior when incorrect number of command-line arguments is provided.

    This test verifies that the tool properly handles missing arguments,
    ensuring it exits with the correct error code and message.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 2
        - Error message indicates missing required argument
    """
    test_args = ["p2p.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 2
        captured = capsys.readouterr()
        assert "required" in captured.err


def test_same_extension(capsys):
    """
    Test behavior when source and destination files have the same extension.

    This test ensures that the tool properly validates file extensions,
    requiring different extensions for source and destination files.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 1
        - Error message indicates invalid extension combination
    """
    test_args = ["p2p.py", "source.py", "destination.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert (
            "Error: Source and destination files must have different extensions (.py or .pi)"
            in captured.out
        )


def test_invalid_extension(capsys):
    """
    Test behavior when files have invalid extensions.

    This test verifies that the tool properly validates file extensions,
    requiring either .py or .pi extensions for both files.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 1
        - Error message indicates invalid file extensions
    """
    test_args = ["p2p.py", "source.txt", "destination.pi"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert (
            "Error: Both files must have either .py or .pi extensions" in captured.out
        )


def test_file_not_found(capsys):
    """
    Test behavior when the source file does not exist.

    This test verifies that the tool properly handles non-existent input files,
    providing appropriate error messages and exit codes.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 1
        - Error message indicates file not found
    """
    test_args = ["p2p.py", "nonexistent.pi", "destination.py"]
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

    This test ensures that the tool properly handles I/O errors when reading
    the source file, providing appropriate error messages and exit codes.

    Args:
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Exits with SystemExit code 1
        - Error message indicates file read error
    """
    test_args = ["p2p.py", "source.pi", "destination.py"]
    with patch.object(sys, "argv", test_args):
        with patch("builtins.open", mock_open()) as mocked_open:
            mocked_open.side_effect = IOError
            with pytest.raises(SystemExit) as e:
                main()
            assert e.type == SystemExit
            assert e.value.code == 1
            captured = capsys.readouterr()
            assert "Error: Unable to read input file 'source.pi'." in captured.out


def test_bidirectional_translation(tmp_path, capsys):
    """
    Test complete bidirectional translation workflow.

    This test verifies the full translation cycle:
    1. Python -> Piyathon translation
    2. Piyathon -> Python translation
    3. Comparison of original and final Python code

    The test uses temporary files to avoid affecting the actual filesystem
    and ensures proper cleanup.

    Args:
        tmp_path: pytest fixture for temporary directory
        capsys: pytest fixture for capturing stdout/stderr

    Assertions:
        - Successful translation in both directions
        - Content preservation through translation cycle
        - Proper file creation and cleanup
        - Correct success messages
    """
    # Create temporary files
    source_py = tmp_path / "p2p.py"
    intermediate_pi = tmp_path / "p2p.pi"
    final_py = tmp_path / "p2p_final.py"

    # Copy original p2p.py content to temp file
    with open("piyathon/p2p.py", "r", encoding="utf-8") as f:
        original_content = f.read()
    source_py.write_text(original_content, encoding="utf-8")

    # Python -> Piyathon
    test_args = ["p2p.py", str(source_py), str(intermediate_pi)]
    with patch.object(sys, "argv", test_args):
        main()
    captured = capsys.readouterr()
    assert "Python to Piyathon translation completed." in captured.out
    assert intermediate_pi.exists()

    # Piyathon -> Python
    test_args = ["p2p.py", str(intermediate_pi), str(final_py)]
    with patch.object(sys, "argv", test_args):
        main()
    captured = capsys.readouterr()
    assert "Piyathon to Python translation completed." in captured.out
    assert final_py.exists()

    # Compare original and final Python code
    final_content = final_py.read_text(encoding="utf-8")
    assert original_content == final_content

    # Verify files exist before cleanup
    assert source_py.exists()
    assert intermediate_pi.exists()
    assert final_py.exists()
