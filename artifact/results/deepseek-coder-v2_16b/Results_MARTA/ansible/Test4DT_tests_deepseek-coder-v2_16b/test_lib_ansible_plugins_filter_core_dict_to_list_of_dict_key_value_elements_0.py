
import pytest
from ansible.plugins.filter.core import dict_to_list_of_dict_key_value_elements, AnsibleFilterTypeError
from collections.abc import Mapping

# Test Scenario 1: Test standard input with a valid dictionary
def test_valid_input():
    mydict = {'a': 1, 'b': 2}
    result = dict_to_list_of_dict_key_value_elements(mydict)
    assert isinstance(result, list), "Expected a list"
    assert all(isinstance(item, dict) for item in result), "All items should be dictionaries"
    assert len(result) == 2, "Expected two dictionaries"
    assert all('key' in item and 'value' in item for item in result), "Each dictionary should have 'key' and 'value'"
    assert result == [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}], "Expected specific dictionaries"

# Test Scenario 2: Test custom key and value names
def test_custom_keys():
    mydict = {'foo': 10, 'bar': 20}
    result = dict_to_list_of_dict_key_value_elements(mydict, key_name='custom_key', value_name='custom_value')
    assert isinstance(result, list), "Expected a list"
    assert all(isinstance(item, dict) for item in result), "All items should be dictionaries"
    assert len(result) == 2, "Expected two dictionaries"
    assert all('custom_key' in item and 'custom_value' in item for item in result), "Each dictionary should have 'custom_key' and 'custom_value'"
    assert result == [{'custom_key': 'foo', 'custom_value': 10}, {'custom_key': 'bar', 'custom_value': 20}], "Expected specific dictionaries"

# Test Scenario 3: Test handling of non-dictionary input by raising AnsibleFilterTypeError
def test_invalid_input():
    mylist = [1, 2, 3]
    with pytest.raises(AnsibleFilterTypeError):
        dict_to_list_of_dict_key_value_elements(mylist)
