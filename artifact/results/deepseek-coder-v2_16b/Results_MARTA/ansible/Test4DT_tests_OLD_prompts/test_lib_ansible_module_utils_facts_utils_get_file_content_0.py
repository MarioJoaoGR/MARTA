
import os
import fcntl
from unittest.mock import patch, MagicMock
import pytest
from ansible.module_utils.facts.utils import get_file_content

@pytest.fixture(autouse=True)
def mock_open():
    with patch('builtins.open', create=True) as mock_file:
        yield mock_file

def test_valid_input():
    with patch('os.path.exists', return_value=True):
        with patch('os.access', return_value=True):
            mock_file = MagicMock()
            mock_file.__enter__.return_value = mock_file
            mock_file.read.return_value = "test content"
            
            with patch('builtins.open', return_value=mock_file):
                result = get_file_content('valid_path', strip=True)
                assert result == "test content"

def test_invalid_path():
    with patch('os.path.exists', return_value=False):
        result = get_file_content('invalid_path', default='default content', strip=True)
        assert result == 'default content'

def test_empty_file(mock_open):
    mock_file = MagicMock()
    mock_file.__enter__.return_value = mock_file
    mock_file.read.return_value = ""
    mock_open.return_value = mock_file
    
    result = get_file_content('empty_path', default='default content', strip=True)
    assert result == 'default content'
