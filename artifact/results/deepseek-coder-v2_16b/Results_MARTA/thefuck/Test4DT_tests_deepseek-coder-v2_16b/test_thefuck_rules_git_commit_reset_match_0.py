
import pytest
from unittest.mock import patch
from thefuck.rules.git_commit_reset import match
from thefuck.types import Command

# Test scenario 1: Valid input where command contains 'commit'
def test_valid_input():
    with patch('thefuck.rules.git_commit_reset.match', return_value=True):
        command = Command("git commit -m 'Add new feature'", "")
        assert match(command) is True

# Test scenario 2: Command does not contain 'commit'
def test_no_commit():
    with patch('thefuck.rules.git_commit_reset.match', return_value=False):
        command = Command("ls -l", "")
        assert match(command) is False

# Test scenario 3: Empty command
def test_empty_command():
    with patch('thefuck.rules.git_commit_reset.match', return_value=False):
        command = Command("", "")
        assert match(command) is False
