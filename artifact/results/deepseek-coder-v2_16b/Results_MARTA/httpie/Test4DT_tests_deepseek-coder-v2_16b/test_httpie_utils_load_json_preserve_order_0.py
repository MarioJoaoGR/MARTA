
import json
from collections import OrderedDict
import pytest

def load_json_preserve_order(s):
    return json.loads(s, object_pairs_hook=OrderedDict)

# Test Scenario 1: Test standard input with valid JSON string
def test_valid_json_string():
    json_string = '{"name": "Alice", "age": 30, "city": "Wonderland"}'
    result = load_json_preserve_order(json_string)
    assert isinstance(result, OrderedDict)
    assert list(result.keys()) == ['name', 'age', 'city']
    assert result['name'] == 'Alice'
    assert result['age'] == 30
    assert result['city'] == 'Wonderland'

# Test Scenario 2: Test handling of None input
def test_none_input():
    s = None
    with pytest.raises(TypeError):
        load_json_preserve_order(s)

# Test Scenario 3: Test raising ValueError with invalid JSON string
def test_invalid_json_string():
    invalid_json_string = '{"name": "Alice", "age": 30, "city": Wonderland}'
    with pytest.raises(ValueError):
        load_json_preserve_order(invalid_json_string)
