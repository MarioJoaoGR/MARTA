
import pytest
import json
from collections import OrderedDict
import click
from unittest.mock import patch

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

@pytest.mark.parametrize("input_data", [
    ('{"name": "John", "age": 30}'),
])
def test_valid_input(input_data):
    result = process_json(input_data)
    assert isinstance(result, OrderedDict)
    assert list(result.keys()) == ['name', 'age']
    assert result['name'] == 'John'
    assert result['age'] == 30

@pytest.mark.parametrize("input_data", [
    (None),
])
def test_none_input(input_data):
    with pytest.raises(click.UsageError):
        process_json(input_data)

@pytest.mark.parametrize("input_data", [
    ('{"name": "John", "age": thirty}'),
])
def test_invalid_json(input_data):
    with pytest.raises(click.UsageError):
        process_json(input_data)
