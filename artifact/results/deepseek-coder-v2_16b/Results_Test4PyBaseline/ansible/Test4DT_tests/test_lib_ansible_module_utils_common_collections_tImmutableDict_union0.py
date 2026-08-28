
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization of ImmutableDict with initial key-value pairs
def test_init_with_dict():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert isinstance(immutable_dict, ImmutableDict)
    assert len(immutable_dict._store) == 2
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'

# Test initialization of ImmutableDict with keyword arguments
def test_init_with_kwargs():
    immutable_dict = ImmutableDict(key1='value1', key2='value2')
    assert isinstance(immutable_dict, ImmutableDict)
    assert len(immutable_dict._store) == 2
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'

# Test accessing values by key
def test_get():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'
    with pytest.raises(KeyError):
        immutable_dict.get('non_existent_key')

# Test iterating over keys and values
def test_items():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    items = list(immutable_dict.items())
    assert len(items) == 2
    assert ('key1', 'value1') in items
    assert ('key2', 'value2') in items

# Test combining dictionaries with union method
def test_union():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    overriding_dict = {'key3': 'value3', 'key4': 'value4'}
    combined_dict = immutable_dict.union(overriding_dict)
    assert isinstance(combined_dict, ImmutableDict)
    assert len(combined_dict._store) == 4
    assert combined_dict.get('key1') == 'value1'
    assert combined_dict.get('key2') == 'value2'
    assert combined_dict.get('key3') == 'value3'
    assert combined_dict.get('key4') == 'value4'

# Test that attempting to update the dictionary raises a TypeError
def test_immutable():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'
