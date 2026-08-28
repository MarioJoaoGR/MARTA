
import pytest
from ansible.module_utils.common.collections import ImmutableDict

# Scenario 1: Test valid inputs
def test_valid_inputs():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable_dict['key1'] == 'value1'
    assert immutable_dict['key2'] == 'value2'

# Scenario 2: Test edge cases, including None and empty values
def test_edge_cases():
    with pytest.raises(AttributeError):
        immutable_dict = ImmutableDict()
        immutable_dict.__setitem__('new_key', 'new_value')

# Scenario 3: Test raising AttributeError for update attempts
def test_invalid_inputs():
    immutable_dict = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    with pytest.raises(AttributeError):
        immutable_dict.update({'new_key': 'new_value'})
