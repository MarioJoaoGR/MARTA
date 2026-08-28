
import pytest
from httpie.utils import load_json_preserve_order
import json
from collections import OrderedDict

def test_load_json_preserve_order_valid():
    valid_json_string = '{"name": "Alice", "age": 30, "city": "Wonderland"}'
    result = load_json_preserve_order(valid_json_string)
    assert isinstance(result, OrderedDict)
    assert list(result.keys()) == ['name', 'age', 'city']
    assert result['name'] == 'Alice'
    assert result['age'] == 30
    assert result['city'] == 'Wonderland'
