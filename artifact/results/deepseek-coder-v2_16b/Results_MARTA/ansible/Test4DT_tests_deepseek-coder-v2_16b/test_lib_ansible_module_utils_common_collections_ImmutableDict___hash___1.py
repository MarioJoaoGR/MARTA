
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test Scenario 1: Test standard input with valid key-value pairs
def test_valid_input():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    assert immutable_dict['key2'] == 'value2'

# Test Scenario 2: Test handling of None input
def test_none_input():
    with pytest.raises(TypeError):
        ImmutableDict(None)

# Test Scenario 3: Test attempting to update the dictionary, expecting AttributeError
def test_invalid_update():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(AttributeError):
        immutable_dict.__setitem__('new_key', 'new_value')
