
import pytest
from unittest.mock import patch, mock_open
from cookiecutter.replay import load

# Mock JSON data for testing
MOCK_JSON_DATA = '{"cookiecutter": {"key1": "value1", "key2": "value2"}}'
INVALID_JSON_DATA_NO_COOKIECUTTER = '{"other_key": {"key1": "value1", "key2": "value2"}}'

def test_load_valid_file():
    with patch('builtins.open', mock_open(read_data=MOCK_JSON_DATA)):
        context = load('/path/to/directory', 'data')
        assert context == {'cookiecutter': {'key1': 'value1', 'key2': 'value2'}}

def test_load_with_json_extension():
    with patch('builtins.open', mock_open(read_data=MOCK_JSON_DATA)):
        context = load('/another/path', 'config.json')