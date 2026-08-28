
import pytest
from unittest.mock import patch
import sys

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

@pytest.fixture
def mock_input():
    with patch('builtins.input', side_effect=['y']):
        yield

@pytest.fixture
def mock_no_input():
    with patch('builtins.input', side_effect=['n']):
        yield

@pytest.fixture
def mock_quit_input():
    with patch('builtins.input', side_effect=['q']):
        yield

def test_valid_input_yes(mock_input):
    assert ask_whether_to_apply_changes_to_file("example.txt") is True

def test_valid_input_no(mock_no_input):
    assert ask_whether_to_apply_changes_to_file("example.txt") is False

def test_invalid_input_quit(mock_quit_input):
    with pytest.raises(SystemExit) as e:
        ask_whether_to_apply_changes_to_file("example.txt")
    assert str(e.value) == '1'
