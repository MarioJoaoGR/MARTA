
import pytest
import click
from unittest.mock import patch
from cookiecutter.prompt import read_user_dict

def process_json(value):
    try:
        return eval(value)
    except Exception as e:
        raise ValueError(f"Invalid JSON: {e}")

# Patch the process_json function to avoid using eval in tests


@patch('cookiecutter.prompt.process_json', side_effect=lambda x: json.loads(x) if x != 'default' else {})
def test_default_input(mock_process_json):
    with patch.object(click, 'prompt', return_value='default'):
        result = read_user_dict("Enter your data:", {"key": "value"})
        assert result == {"key": "value"}



import json