
import pytest
from unittest.mock import patch, mock_open
import json
from cookiecutter.replay import load

# Test cases for the load function
def test_load_basic():
    with patch('builtins.open', mock_open(read_data=json.dumps({'cookiecutter': {}}))):
        result = load('data', 'replay')
        assert isinstance(result, dict)
        assert 'cookiecutter' in result

def test_load_with_full_path():
    with patch('builtins.open', mock_open(read_data=json.dumps({'cookiecutter': {}}))):
        result = load('logs/', 'errorlog')
        assert isinstance(result, dict)
        assert 'cookiecutter' in result

def test_load_with_explicit_extension():
    with patch('builtins.open', mock_open(read_data=json.dumps({'cookiecutter': {}}))):
        result = load('backups', 'config')
        assert isinstance(result, dict)