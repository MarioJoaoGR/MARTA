
import sys
from unittest.mock import patch
import pytest

def ask_whether_to_apply_changes_to_file(file_path: str) -> bool:
    answer = None
    while answer not in ("yes", "y", "no", "n", "quit", "q"):
        answer = input(f"Apply suggested changes to '{file_path}' [y/n/q]? ")  # nosec
        answer = answer.lower()
        if answer in ("no", "n"):
            return False
        if answer in ("quit", "q"):
            sys.exit(1)
    return True

def test_apply_changes_yes():
    with patch('builtins.input', return_value='yes'):
        assert ask_whether_to_apply_changes_to_file("example.txt") is True

def test_apply_changes_y():
    with patch('builtins.input', return_value='y'):
        assert ask_whether_to_apply_changes_to_file("example.txt") is True

def test_apply_changes_no():
    with patch('builtins.input', return_value='no'):
        assert ask_whether_to_apply_changes_to_file("example.txt") is False

def test_apply_changes_n():
    with patch('builtins.input', return_value='n'):
        assert ask_whether_to_apply_changes_to_file("example.txt") is False

def test_apply_changes_quit():
    with pytest.raises(SystemExit) as excinfo:
        with patch('builtins.input', return_value='quit'):
            ask_whether_to_apply_changes_to_file("example.txt")
    assert excinfo.value.code == 1

def test_apply_changes_q():
    with pytest.raises(SystemExit) as excinfo:
        with patch('builtins.input', return_value='q'):
            ask_whether_to_apply_changes_to_file("example.txt")
    assert excinfo.value.code == 1
