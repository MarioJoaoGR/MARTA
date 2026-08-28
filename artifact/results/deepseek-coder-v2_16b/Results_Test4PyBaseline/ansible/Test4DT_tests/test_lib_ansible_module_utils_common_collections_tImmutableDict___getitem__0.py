# Module: ansible.module_utils.common.collections
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization with dictionary literal
def test_initialization_with_dict_literal():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    for key, value in immutable_dict.items():
        assert key in ['key1', 'key2'] and value == {'key1': 'value1', 'key2': 'value2'}[key]

# Test initialization with keyword arguments
def test_initialization_with_keyword_args():
    immutable_dict = ImmutableDict(key1='value1', key2='value2')
    assert immutable_dict['key1'] == 'value1'
    for key, value in immutable_dict.items():
        assert key in ['key1', 'key2'] and value == {'key1': 'value1', 'key2': 'value2'}[key]

# Test accessing values by key
def test_accessing_values_by_key():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    assert immutable_dict['key2'] == 'value2'

# Test iterating over keys and values
def test_iterating_over_keys_and_values():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    expected_items = {'key1': 'value1', 'key2': 'value2'}
    for key, value in immutable_dict.items():
        assert key in expected_items and value == expected_items[key]

# Test trying to update the dictionary (should raise TypeError)
def test_updating_the_dictionary():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'
