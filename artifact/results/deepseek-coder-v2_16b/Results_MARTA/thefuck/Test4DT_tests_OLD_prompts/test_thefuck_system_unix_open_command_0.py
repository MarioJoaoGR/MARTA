
import pytest
from unittest.mock import patch, MagicMock
from thefuck.system.unix import find_executable

def open_command(arg):
    if find_executable('xdg-open'):
        return 'xdg-open ' + arg
    return 'open ' + arg

@patch('thefuck.system.unix.find_executable')
def test_valid_input_file(mock_find_executable):
    mock_find_executable.return_value = False  # Mock that 'xdg-open' is not available
    result = open_command('report.html')
    assert result == 'open report.html'

@patch('thefuck.system.unix.find_executable')
def test_valid_input_url(mock_find_executable):
    mock_find_executable.return_value = False  # Mock that 'xdg-open' is not available
    result = open_command('http://example.com')
    assert result == 'open http://example.com'

@patch('thefuck.system.unix.find_executable')
def test_missing_xdg_open(mock_find_executable):
    mock_find_executable.return_value = None  # Mock that 'xdg-open' is not found on the system
    result = open_command('report.html')
    assert result == 'open report.html'
