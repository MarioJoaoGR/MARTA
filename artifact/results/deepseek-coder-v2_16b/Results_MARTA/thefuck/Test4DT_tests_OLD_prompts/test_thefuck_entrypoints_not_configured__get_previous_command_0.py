
import pytest
from unittest.mock import patch, MagicMock
from thefuck.entrypoints.not_configured import _get_previous_command

# Test when there is no history
def test_no_history():
    with patch('thefuck.entrypoints.not_configured.shell.get_history', return_value=[]):
        assert _get_previous_command() is None

# Test when there is a history entry
def test_with_history():
    mock_history = ["echo Hello", "ls -l"]
    with patch('thefuck.entrypoints.not_configured.shell.get_history', return_value=mock_history):
        assert _get_previous_command() == "ls -l"
