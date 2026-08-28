
import pytest
from unittest.mock import patch
from thefuck.rules.git_commit_reset import match
from thefuck.types import Command

# Test scenario 1: test_valid_input
def test_valid_input():
    command = Command('git commit -m "Add new feature"', '')
    with patch('thefuck.rules.git_commit_reset.match', return_value=True):
        assert match(command) is True

# Test scenario 2: test_no_commit
def test_no_commit():
    command = Command('ls -l', '')
    with patch('thefuck.rules.git_commit_reset.match', return_value=False):
        assert match(command) is False

# Test scenario 3: test_empty_command
def test_empty_command():
    command = Command('', '')
    with patch('thefuck.rules.git_commit_reset.match', return_value=False):
        assert match(command) is False
