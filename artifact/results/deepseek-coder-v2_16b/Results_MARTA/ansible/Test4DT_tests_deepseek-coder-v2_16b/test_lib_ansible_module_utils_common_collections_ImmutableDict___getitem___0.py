
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Test scenario 1: test_valid_input
def test_valid_input():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    assert immutable_dict['key2'] == 'value2'

# Test scenario 2: test_error_handling
def test_error_handling():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(AttributeError):
        immutable_dict.__setitem__('new_key', 'new_value')

# Test scenario 3: test_empty_initialization
def test_empty_initialization():
    immutable_dict = ImmutableDict()
    assert len(immutable_dict) == 0
