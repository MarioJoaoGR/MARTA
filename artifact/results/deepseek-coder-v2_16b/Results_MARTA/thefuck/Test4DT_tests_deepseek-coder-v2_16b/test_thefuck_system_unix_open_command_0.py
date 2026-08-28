
import pytest
from unittest.mock import patch
from thefuck.system.unix import find_executable, open_command

def test_valid_input_file():
    with patch('thefuck.system.unix.find_executable', return_value=True):
        result = open_command('report.html')
        assert result == 'xdg-open report.html' or result == 'open report.html'

def test_valid_input_url():
    with patch('thefuck.system.unix.find_executable', return_value=True):
        result = open_command('http://example.com')
        assert result == 'xdg-open http://example.com' or result == 'open http://example.com'

def test_missing_xdg_open():
    with patch('thefuck.system.unix.find_executable', return_value=False):
        result = open_command('report.html')
        assert result == 'open report.html'
