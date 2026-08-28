
import pytest
from ansible.vars.manager import preprocess_vars
from collections.abc import MutableMapping
from ansible.errors import AnsibleError

def test_preprocess_vars_none():
    assert preprocess_vars(None) is None

def test_preprocess_vars_single_dict():
    input_data = {'key': 'value'}
    expected_output = [{'key': 'value'}]
    assert preprocess_vars(input_data) == expected_output

def test_preprocess_vars_list_of_dicts():
    input_data = [{'key1': 'value1'}, {'key2': 'value2'}]
    expected_output = [{'key1': 'value1'}, {'key2': 'value2'}]
    assert preprocess_vars(input_data) == expected_output

def test_preprocess_vars_invalid_input():
    input_data = "not a list or dict"
    with pytest.raises(AnsibleError):
        preprocess_vars(input_data)
