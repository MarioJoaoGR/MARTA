
import os
from unittest.mock import patch, MagicMock
import pytest
from cookiecutter.repository import repository_has_cookiecutter_json

# Test for valid case where the directory and 'cookiecutter.json' file exist
def test_valid_case():
    with patch('os.path.isdir', return_value=True):
        with patch('os.path.isfile', return_value=True):
            assert repository_has_cookiecutter_json('/path/to/repo') is True

# Test for case where the directory exists but 'cookiecutter.json' file does not exist
def test_missing_file():
    with patch('os.path.isdir', return_value=True):
        with patch('os.path.isfile', return_value=False):
            assert repository_has_cookiecutter_json('/path/to/repo') is False

# Test for case where the directory does not exist
def test_missing_directory():
    with patch('os.path.isdir', return_value=False):
        assert repository_has_cookiecutter_json('/nonexistent/directory') is False

# Test for invalid input (None)
def test_invalid_input():
    with pytest.raises(TypeError):
        repository_has_cookiecutter_json(None)
