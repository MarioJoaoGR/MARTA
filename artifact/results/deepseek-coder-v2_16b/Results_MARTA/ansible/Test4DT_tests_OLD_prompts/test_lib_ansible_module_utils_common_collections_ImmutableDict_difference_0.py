
import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_invalid_input():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    with pytest.raises(TypeError):
        original_dict['new_key'] = 'new_value'  # This should raise a TypeError

def test_access_existing_key():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    assert original_dict['key1'] == 'value1'  # This should access the existing key without raising an error

def test_access_nonexistent_key():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    with pytest.raises(KeyError):
        value = original_dict['key4']  # This should raise a KeyError

def test_difference():
    original_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    filtered_dict = original_dict.difference(['key1'])
    assert len(filtered_dict) == 2  # The key1 should be removed, so the length should be 2
    with pytest.raises(KeyError):
        value = filtered_dict['key1']  # This should raise a KeyError because key1 is not in the dictionary anymore
