
import pytest
from unittest.mock import patch
import json
from cookiecutter.prompt import read_user_dict

def process_json(value):
    if value == 'default':
        return {}
    try:
        return json.loads(value)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON: {e}")

# Patching the process_json function to avoid actual JSON parsing during tests





@patch('cookiecutter.prompt.process_json', side_effect=process_json)
def test_default_input(mock_process_json):
    with patch('cookiecutter.prompt.click.prompt', return_value='default'):
        result = read_user_dict("Enter your data:", {"key": "value"})
        assert result == {"key": "value"}