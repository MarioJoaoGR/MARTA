
# Module: ansible.module_utils.common.collections
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization with a dictionary
def test_initialization_with_dict():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    items = dict(immutable_dict.items())
    assert items == {'key1': 'value1', 'key2': 'value2'}

# Test initialization with keyword arguments
def test_initialization_with_kwargs():
    immutable_dict = ImmutableDict(key1='value1', key2='value2')
    assert immutable_dict['key1'] == 'value1'
    items = dict(immutable_dict.items())
    assert items == {'key1': 'value1', 'key2': 'value2'}

# Test initialization with positional arguments
def test_initialization_with_args():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    items = dict(immutable_dict.items())
    assert items == {'key1': 'value1', 'key2': 'value2'}

# Test attempting to update the dictionary raises TypeError
def test_attempting_to_update_raises_type_error():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'

# Test __eq__ method with identical objects
def test_equality_with_identical_objects():
    dict1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    dict2 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert dict1 == dict2

# Test __eq__ method with different objects
def test_equality_with_different_objects():
    dict1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    dict2 = ImmutableDict({'key1': 'value1', 'key2': 'other_value'})
    assert not (dict1 == dict2)

# Test __eq__ method with non-ImmutableDict objects
def test_equality_with_non_immutable_dict():
    dict1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    dict2 = {'key1': 'value1', 'key2': 'value2'}
    assert not (dict1 == dict2)

# Test __eq__ method with None
def test_equality_with_none():
    dict1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert not (dict1 == None)
