
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test initialization with initial key-value pairs
def test_initialization():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert isinstance(immutable_dict, ImmutableDict)
    assert len(immutable_dict._store) == 2
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'

# Test accessing values by key
def test_accessing_values():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict.get('key1') == 'value1'
    assert immutable_dict.get('key2') == 'value2'
    with pytest.raises(KeyError):
        immutable_dict['non_existent_key']  # This should raise a KeyError

# Test iterating over all keys and values
def test_iterating_over_keys_and_values():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    items = list(immutable_dict.items())
    assert len(items) == 2
    assert ('key1', 'value1') in items
    assert ('key2', 'value2') in items

# Test creating a new ImmutableDict by excluding specific keys
def test_difference():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    modified_immutable_dict = immutable_dict.difference(['key1'])
    assert isinstance(modified_immutable_dict, ImmutableDict)
    assert len(modified_immutable_dict._store) == 1
    assert modified_immutable_dict.get('key2') == 'value2'
    with pytest.raises(KeyError):
        modified_immutable_dict['key1']  # This should raise a KeyError

# Test raising TypeError when attempting to update the dictionary
def test_updating_dictionary():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(TypeError):
        immutable_dict['new_key'] = 'new_value'  # This should raise a TypeError

# Test the difference method with keys that do not exist in the original dictionary
def test_difference_with_nonexistent_keys():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    modified_immutable_dict = immutable_dict.difference(['non_existent_key'])
    assert isinstance(modified_immutable_dict, ImmutableDict)
    assert len(modified_immutable_dict._store) == 2  # The original keys should remain unchanged
    assert modified_immutable_dict.get('key1') == 'value1'
    assert modified_immutable_dict.get('key2') == 'value2'
    with pytest.raises(KeyError):
        modified_immutable_dict['non_existent_key']  # This should raise a KeyError

# Test the difference method with an empty list
def test_difference_with_empty_list():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    modified_immutable_dict = immutable_dict.difference([])
    assert isinstance(modified_immutable_dict, ImmutableDict)
    assert len(modified_immutable_dict._store) == 2  # The original keys should remain unchanged
    assert modified_immutable_dict.get('key1') == 'value1'
    assert modified_immutable_dict.get('key2') == 'value2'

# Test the difference method with a mix of existing and nonexistent keys
def test_difference_with_mixed_keys():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    modified_immutable_dict = immutable_dict.difference(['key1', 'non_existent_key'])
    assert isinstance(modified_immutable_dict, ImmutableDict)
    assert len(modified_immutable_dict._store) == 1  # Only key2 should remain
    assert modified_immutable_dict.get('key2') == 'value2'
    with pytest.raises(KeyError):
        modified_immutable_dict['key1']  # This should raise a KeyError
