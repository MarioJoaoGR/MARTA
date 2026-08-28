# Module: ansible.module_utils.common.collections
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization with a dictionary
def test_initialization_with_dict():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    for key, value in immutable_dict.items():
        print(f"{key}: {value}")  # Output: key1: value1, key2: value2

# Test initialization with keyword arguments
def test_initialization_with_kwargs():
    immutable_dict = ImmutableDict(key1='value1', key2='value2')
    assert immutable_dict['key1'] == 'value1'
    for key, value in immutable_dict.items():
        print(f"{key}: {value}")  # Output: key1: value1, key2: value2

# Test initialization with positional and keyword arguments
def test_initialization_with_args_and_kwargs():
    immutable_dict = ImmutableDict({'key1': 'value1'}, key2='value2')
    assert immutable_dict['key1'] == 'value1'
    for key, value in immutable_dict.items():
        print(f"{key}: {value}")  # Output: key1: value1, key2: value2

# Test attempting to update the dictionary raises TypeError
def test_updating_immutable_dict():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'
