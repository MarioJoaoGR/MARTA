
import pytest
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

# Test scenarios
def test_valid_input():
    json_data = '{"name": "John", "age": 30}'
    result = process_json(json_data)
    assert isinstance(result, OrderedDict)
    assert result == OrderedDict([('name', 'John'), ('age', 30)])

def test_none_input():
    user_value = None
    with pytest.raises(click.UsageError):
        process_json(user_value)

def test_invalid_json():
    invalid_json_data = '{"name": "John", "age": thirty}'
    with pytest.raises(click.UsageError):
        process_json(invalid_json_data)
