
# Module: ansible.module_utils.common.collections
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization with key-value pairs
def test_initialization():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert isinstance(immutable_dict, ImmutableDict)
    assert len(immutable_dict._store) == 2
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'

# Test accessing a value by its key
def test_accessing_value():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'

# Test iterating over keys and values
def test_iterating_over_items():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    items = list(immutable_dict.items())
    assert len(items) == 2
    assert ('key1', 'value1') in items
    assert ('key2', 'value2') in items

# Test attempting to update the dictionary, which should raise a TypeError
def test_attempting_to_update():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'

# Test the __iter__ method to ensure it supports iteration over keys and values
def test_iteration():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    # Check iteration over keys
    keys = [key for key in immutable_dict]
    assert len(keys) == 2
    assert 'key1' in keys
    assert 'key2' in keys
    
    # Check iteration over values
    values = [value for value in immutable_dict.values()]
    assert len(values) == 2
    assert 'value1' in values
    assert 'value2' in values
