
import pytest
from httpie.cli.requestitems import load_json, KeyValueArg
from collections import OrderedDict
import json
from unittest.mock import patch

# Test for invalid JSON string input

# Test for valid JSON string input
def test_load_json_valid():
    arg = KeyValueArg(key=None, value=None, sep='', orig='in-memory')
    contents = '{"name": "Alice", "age": 30, "city": "Wonderland"}'
    result = load_json(arg, contents)
    assert isinstance(result, OrderedDict)
    assert list(result.keys()) == ['name', 'age', 'city']
    assert list(result.values()) == ['Alice', 30, 'Wonderland']

# Test for invalid JSON file path input (mocking open function to raise FileNotFoundError)

# Test for valid JSON file path input (mocking open function to return valid content)