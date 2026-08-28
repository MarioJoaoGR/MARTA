
import pytest
from unittest.mock import patch, MagicMock
import json
from collections import OrderedDict
import click

def process_json(user_value):
    """Load user-supplied value as a JSON dict.

    :param str user_value: User-supplied value to load as a JSON dict
    """
    try:
        user_dict = json.loads(user_value, object_pairs_hook=OrderedDict)
    except Exception:
        # Leave it up to click to ask the user again
        raise click.UsageError('Unable to decode to JSON.')

    if not isinstance(user_dict, dict):
        # Leave it up to click to ask the user again
        raise click.UsageError('Requires JSON dict.')

    return user_dict

@pytest.fixture
def valid_json():
    return '{"name": "John", "age": 30}'

@pytest.fixture
def none_input():
    return None

@pytest.fixture
def invalid_json():
    return '{"name": "John", "age": thirty}'

def test_valid_input(valid_json):
    with patch('builtins.input', return_value=valid_json):
        result = process_json(input())
        assert isinstance(result, OrderedDict)
        assert len(result) == 2
        assert 'name' in result and result['name'] == 'John'
        assert 'age' in result and result['age'] == 30

def test_none_input(none_input):
    with pytest.raises(click.UsageError):
        process_json(none_input)

def test_invalid_json(invalid_json):
    with patch('builtins.input', return_value=invalid_json):
        with pytest.raises(click.UsageError):
            process_json(input())
