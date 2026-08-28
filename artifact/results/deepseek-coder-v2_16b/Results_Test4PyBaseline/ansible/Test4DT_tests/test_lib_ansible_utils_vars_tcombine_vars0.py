# Module: ansible.utils.vars
import pytest
from ansible.utils.vars import combine_vars, merge_hash

# Helper function to validate mutable mappings
def _validate_mutable_mappings(*dicts):
    for d in dicts:
        if not isinstance(d, dict):
            raise ValueError("All arguments must be dictionaries")

# Test cases for combine_vars function
@pytest.mark.parametrize("a, b, merge, expected", [
    ({'key1': 'value1', 'key2': 'value2'}, {'key3': 'value3', 'key4': 'value4'}, None, {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}),
    ({'key1': 'value1', 'sub_dict': {'sub_key1': 'sub_value1'}}, {'key2': 'value2', 'sub_dict': {'sub_key2': 'sub_value2'}}, 'merge', {'key1': 'value1', 'key2': 'value2', 'sub_dict': {'sub_key1': 'sub_value1', 'sub_key2': 'sub_value2'}}),
    ({'key1': 'value1'}, {'key2': 'value2', 'key3': 'value3'}, None, {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}),
    ({'key1': 'value1', 'sub_dict': {'sub_key1': 'sub_value1'}}, {'key2': 'value2', 'sub_dict': {'sub_key2': 'sub_value2'}}, 'replace', {'key1': 'value1', 'key2': 'value2', 'sub_dict': {'sub_key2': 'sub_value2'}})
])
def test_combine_vars(a, b, merge, expected):
    result = combine_vars(a, b, merge)
    assert result == expected

# Test case for invalid input types
@pytest.mark.parametrize("a, b", [
    ({'key1': 'value1'}, 123),
    (123, {'key2': 'value2'})
])
def test_combine_vars_invalid_input(a, b):
    with pytest.raises(ValueError):
        combine_vars(a, b)
