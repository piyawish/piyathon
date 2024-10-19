# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import sys
from unittest.mock import patch, mock_open
import pytest
from piyathon.piyathon import main


def test_no_arguments(capsys):
    test_args = ["piyathon.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 2
        captured = capsys.readouterr()
        assert "required" in captured.err


def test_invalid_extension(capsys):
    test_args = ["piyathon.py", "source.txt"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert "Error: The source file must have a .pi extension" in captured.out


def test_file_not_found(capsys):
    test_args = ["piyathon.py", "nonexistent.pi"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert "Error: Input file 'nonexistent.pi' not found." in captured.out


def test_file_read_error(capsys):
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
