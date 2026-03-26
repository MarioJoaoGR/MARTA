# Module: isort.format
import sys
from unittest.mock import patch

import pytest

from isort.format import ask_whether_to_apply_changes_to_file


# Test case 1: User decides to apply the changes
@patch('builtins.input', side_effect=['y'])
def test_ask_whether_to_apply_changes_to_file_yes(mock_input):
    assert ask_whether_to_apply_changes_to_file("example.txt") is True

# Test case 2: User decides not to apply the changes
@patch('builtins.input', side_effect=['n'])
def test_ask_whether_to_apply_changes_to_file_no(mock_input):
    assert ask_whether_to_apply_changes_to_file("example.txt") is False

# Test case 3: User decides to quit the program
@patch('builtins.input', side_effect=['q'])
def test_ask_whether_to_apply_changes_to_file_quit(mock_input):
    with pytest.raises(SystemExit) as excinfo:
        ask_whether_to_apply_changes_to_file("example.txt")
    assert excinfo.value.code == 1
