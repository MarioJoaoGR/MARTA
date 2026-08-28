
import pytest
from httpie.cli.requestitems import KeyValueArg, load_json
from collections import OrderedDict
import json

# Helper function to create a KeyValueArg object for in-memory data
def create_keyvaluearg(orig):
    return KeyValueArg(key=None, value=None, sep='', orig=orig)

# Test loading JSON from an in-memory string
def test_load_json_from_string():
    arg = create_keyvaluearg('')
    json_string = '{"name": "Alice", "age": 30, "city": "Wonderland"}'
    result = load_json(arg, json_string)
    assert isinstance(result, OrderedDict)
    assert list(result.keys()) == ['name', 'age', 'city']
    assert list(result.values()) == ['Alice', 30, 'Wonderland']

# Test loading JSON from a file path (file does not exist in this test case)

# Test loading JSON from a valid file path (file does not exist in this test case)