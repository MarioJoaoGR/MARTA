# Module: isort.format
import sys
from unittest.mock import patch

import pytest

from isort.format import ask_whether_to_apply_changes_to_file


# Test case 1: User confirms to apply changes
def test_ask_whether_to_apply_changes_to_file_yes():
    with patch('builtins.input', side_effect=['y']):
        assert ask_whether_to_apply_changes_to_file("example.txt") is True

# Test case 2: User does not confirm, but also doesn't quit
def test_ask_whether_to_apply_changes_to_file_no():
    with patch('builtins.input', side_effect=['n']):
        assert ask_whether_to_apply_changes_to_file("example.txt") is False

# Test case 3: User decides to quit the program
def test_ask_whether_to_apply_changes_to_file_quit():
    with patch('builtins.input', side_effect=['q']):
        with pytest.raises(SystemExit) as e:
            ask_whether_to_apply_changes_to_file("example.txt")
        assert e.type == SystemExit
        assert e.value.code == 1
