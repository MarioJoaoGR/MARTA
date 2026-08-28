# Module: isort.format
import pytest
from unittest.mock import patch
import sys

# Import the function from the specified module
from isort.format import ask_whether_to_apply_changes_to_file

def test_ask_whether_to_apply_changes_to_file_yes():
    with patch('builtins.input', return_value='yes'):
        assert ask_whether_to_apply_changes_to_file("example.txt") == True

def test_ask_whether_to_apply_changes_to_file_y():
    with patch('builtins.input', return_value='y'):
        assert ask_whether_to_apply_changes_to_file("data/report.csv") == True

def test_ask_whether_to_apply_changes_to_file_no():
    with patch('builtins.input', return_value='no'):
        assert ask_whether_to_apply_changes_to_file("example.txt") == False

def test_ask_whether_to_apply_changes_to_file_n():
    with patch('builtins.input', return_value='n'):
        assert ask_whether_to_apply_changes_to_file("data/report.csv") == False

def test_ask_whether_to_apply_changes_to_file_quit():
    with pytest.raises(SystemExit) as excinfo:
        with patch('builtins.input', return_value='quit'):
            ask_whether_to_apply_changes_to_file("example.txt")
    assert excinfo.value.code == 1

def test_ask_whether_to_apply_changes_to_file_q():
    with pytest.raises(SystemExit) as excinfo:
        with patch('builtins.input', return_value='q'):
            ask_whether_to_apply_changes_to_file("data/report.csv")
    assert excinfo.value.code == 1

def test_ask_whether_to_apply_changes_to_file_invalid_input():
    with patch('builtins.input', side_effect=['invalid', 'y']):
        assert ask_whether_to_apply_changes_to_file("example.txt") == True
