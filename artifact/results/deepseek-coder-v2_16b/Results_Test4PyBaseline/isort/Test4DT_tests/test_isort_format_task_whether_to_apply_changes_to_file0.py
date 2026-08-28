# Module: isort.format
import pytest
from unittest.mock import patch
import sys
from isort.format import ask_whether_to_apply_changes_to_file

# Test case for user confirming to apply changes
def test_ask_whether_to_apply_changes_to_file_yes():
    with patch('builtins.input', side_effect=['y']):
        assert ask_whether_to_apply_changes_to_file("example.txt") == True

# Test case for user confirming not to apply changes
def test_ask_whether_to_apply_changes_to_file_no():
    with patch('builtins.input', side_effect=['n']):
        assert ask_whether_to_apply_changes_to_file("example.txt") == False

# Test case for user deciding to quit the program
def test_ask_whether_to_apply_changes_to_file_quit():
    with patch('builtins.input', side_effect=['q']):
        with pytest.raises(SystemExit) as e:
            ask_whether_to_apply_changes_to_file("example.txt")
        assert e.type == SystemExit
        assert e.value.code == 1
