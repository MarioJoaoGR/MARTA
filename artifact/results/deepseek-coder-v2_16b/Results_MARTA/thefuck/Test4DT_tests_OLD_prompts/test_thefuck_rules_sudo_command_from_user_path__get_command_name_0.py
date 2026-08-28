
import pytest
from unittest.mock import patch, MagicMock
from thefuck.rules.sudo_command_from_user_path import _get_command_name

# Test for extracting command name from error message with "sudo: unknownuser: command not found" pattern
def test_get_command_name_with_known_error():
    command_output = MagicMock()
    command_output.output = "sudo: unknownuser: command not found"
    expected = "unknownuser"
    
    with patch('builtins.input', return_value=command_output):
        result = _get_command_name(command_output)
        assert result == expected

# Test for handling no match or normal output
def test_get_command_name_without_error():
    command_output = MagicMock()
    command_output.output = "This is a normal output without any error message."
    expected = None
    
    with patch('builtins.input', return_value=command_output):
        result = _get_command_name(command_output)
        assert result == expected

# Test for handling empty or null input