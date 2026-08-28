
import pytest
from ansible.plugins.filter.core import FilterModule
import json

# Test scenarios for groupby filter
def do_groupby(data, key):
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("Data must be a list of dictionaries")
    if not isinstance(key, str):
        raise ValueError("Key must be a string")
    
    grouped = {}
    for item in data:
        k = item.get(key)
        if k is None:
            continue
        if k not in grouped:
            grouped[k] = []
        grouped[k].append(item)
    return grouped

def test_valid_case_groupby():
    filter_module = FilterModule()
    data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 30}]
    result = filter_module.filters()['groupby'](data, 'age')
    expected = {30: [{"name": "Alice", "age": 30}, {"name": "Charlie", "age": 30}], 25: [{"name": "Bob", "age": 25}]}
    assert result == expected

def test_edge_case_empty_list():
    filter_module = FilterModule()
    data = []
    with pytest.raises(ValueError):
        filter_module.filters()['groupby'](data, 'age')

def test_invalid_input_none():
    filter_module = FilterModule()
    with pytest.raises(ValueError):
        filter_module.filters()['groupby'](None, 'age')
