
import pytest
import json
from collections import OrderedDict
import click
from cookiecutter.prompt import process_json

# Test cases for process_json function
def test_process_json_valid():
    """Test that a valid JSON string is processed correctly."""
    user_value = '{"name": "John", "age": 30}'
    result = process_json(user_value)
    assert isinstance(result, OrderedDict)
    assert list(result.keys()) == ['name', 'age']
    assert result['name'] == 'John'