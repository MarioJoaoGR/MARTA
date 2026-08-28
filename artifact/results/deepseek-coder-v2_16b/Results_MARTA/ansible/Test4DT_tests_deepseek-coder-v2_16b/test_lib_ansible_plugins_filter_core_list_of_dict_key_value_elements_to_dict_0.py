
import pytest
from ansible.plugins.filter.core import list_of_dict_key_value_elements_to_dict, AnsibleFilterTypeError

# Scenario 1: Test standard input with default keys ('key' and 'value')
def test_valid_case_default_keys():
    mylist = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]
    expected_output = {'a': 1, 'b': 2}
    result = list_of_dict_key_value_elements_to_dict(mylist)
    assert result == expected_output

# Scenario 2: Test standard input with custom keys ('k' and 'v')
def test_valid_case_custom_keys():
    mylist = [{'k': 'foo', 'v': 42}, {'k': 'bar', 'v': 23}]
    expected_output = {'foo': 42, 'bar': 23}
    result = list_of_dict_key_value_elements_to_dict(mylist, key_name='k', value_name='v')
    assert result == expected_output

# Scenario 3: Test raising AnsibleFilterTypeError for incorrect input type (non-list)
def test_error_case_incorrect_input_type():
    mylist = 123  # Incorrect input type, should raise AnsibleFilterTypeError
    with pytest.raises(AnsibleFilterTypeError):
        list_of_dict_key_value_elements_to_dict(mylist)
