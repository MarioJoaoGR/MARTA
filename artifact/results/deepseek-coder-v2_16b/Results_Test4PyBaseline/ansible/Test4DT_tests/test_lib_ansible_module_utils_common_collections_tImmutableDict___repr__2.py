
# Module: ansible.module_utils.common.collections
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization with a dictionary
def test_initialization_with_dict():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert repr(immutable_dict) == "ImmutableDict({'key1': 'value1', 'key2': 'value2'})"

# Test accessing a value by its key
def test_accessing_value_by_key():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'

# Test iterating over all keys and values in the dictionary
def test_iterating_over_items():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    items = list(immutable_dict.items())
    assert len(items) == 2
    assert ('key1', 'value1') in items
    assert ('key2', 'value2') in items

# Test using the get method to retrieve a value
def test_get_method():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict.get('key1') == 'value1'

# Test trying to update the dictionary, which should raise a TypeError
def test_updating_immutable_dict():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'

# Test the representation method of ImmutableDict
def test_repr():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert repr(immutable_dict) == "ImmutableDict({'key1': 'value1', 'key2': 'value2'})"
