
import os
import fcntl
import pytest
from unittest.mock import patch
from your_module_name import get_file_content  # Replace 'your_module_name' with the actual module name where get_file_content is defined

# Test scenarios
def test_valid_input_stripped():
    with patch('builtins.open', create=True) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = "  Content of example.txt  "
        result = get_file_content('example.txt')
        assert result == "Content of example.txt"

def test_valid_input_not_stripped():
    with patch('builtins.open', create=True) as mock_open:
        mock_open.return_value.__enter__.return_value.read.return_value = "  Content of example.txt  "
        result = get_file_content('example.txt', strip=False)
        assert result == "  Content of example.txt  "

def test_invalid_path():
    with patch('os.path.exists', return_value=False):
        result = get_file_content('nonexistent.txt', default='Default Content')
        assert result == 'Default Content'
