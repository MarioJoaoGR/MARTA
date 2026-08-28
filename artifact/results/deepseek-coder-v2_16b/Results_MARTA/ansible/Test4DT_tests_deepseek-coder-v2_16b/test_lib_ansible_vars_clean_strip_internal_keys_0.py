
import pytest
from ansible.vars.clean import strip_internal_keys
from collections import MutableMapping, MutableSequence
import six
from ansible.errors import AnsibleError

# Scenario 1: Test standard input with a dictionary containing internal keys
def test_valid_input_dictionary():
    data = {'a': 1, '_ansible_key': 'value', 'nested': {'_ansible_inner_key': 'inner_value'}}
    expected_output = {'a': 1, 'nested': {}}
    result = strip_internal_keys(data)
    assert result == expected_output

# Scenario 2: Test standard input with a list containing nested dictionaries and lists
def test_valid_input_list():
    data_list = [{'a': 1, '_ansible_key': 'value'}, {'b': 2, '_ansible_other_key': 'other_value'}]
    expected_output = [{'a': 1}, {'b': 2}]
    result = strip_internal_keys(data_list)
    assert result == expected_output

# Scenario 3: Test raising ValueError for non-dictionary/list input
def test_invalid_input():
    non_dict_list = [1, 2, 3]
    with pytest.raises(AnsibleError):
        strip_internal_keys(non_dict_list)
