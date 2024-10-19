# Copyright (c) 2024 Piyawish Piyawat
# Licensed under the MIT License

import sys
from unittest.mock import patch, mock_open
import pytest
from piyathon.p2p import main


def test_wrong_number_of_arguments(capsys):
    test_args = ["p2p.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 2
        captured = capsys.readouterr()
        assert "required" in captured.err


def test_same_extension(capsys):
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
    test_args = ["p2p.py", "nonexistent.pi", "destination.py"]
    with patch.object(sys, "argv", test_args):
        with pytest.raises(SystemExit) as e:
            main()
        assert e.type == SystemExit
        assert e.value.code == 1
        captured = capsys.readouterr()
        assert "Error: Input file 'nonexistent.pi' not found." in captured.out


def test_file_read_error(capsys):
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
