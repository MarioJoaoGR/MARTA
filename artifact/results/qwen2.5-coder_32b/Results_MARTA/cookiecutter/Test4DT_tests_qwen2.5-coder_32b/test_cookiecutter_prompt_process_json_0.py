
import pytest
from collections import OrderedDict
import json
from cookiecutter.prompt import click

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

def test_process_json_basic():
    """Test basic functionality of process_json with valid input."""
    user_value = '{"name": "Alice", "age": 30}'
    expected_output = OrderedDict([('name', 'Alice'), ('age', 30)])
    
    assert process_json(user_value) == expected_output
