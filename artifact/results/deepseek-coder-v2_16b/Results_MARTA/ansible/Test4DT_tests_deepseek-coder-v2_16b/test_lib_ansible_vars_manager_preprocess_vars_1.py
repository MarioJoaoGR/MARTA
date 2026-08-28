
import pytest
from ansible.errors import AnsibleError
from collections.abc import MutableMapping

def preprocess_vars(a):
    '''
    Ensures that vars contained in the parameter passed in are
    returned as a list of dictionaries, to ensure for instance
    that vars loaded from a file conform to an expected state.
    '''

    if a is None:
        return None
    elif not isinstance(a, list):
        data = [a]
    else:
        data = a

    for item in data:
        if not isinstance(item, MutableMapping):
            raise AnsibleError("variable files must contain either a dictionary of variables, or a list of dictionaries. Got: %s (%s)" % (a, type(a)))

    return data

# Test cases for preprocess_vars function

def test_preprocess_vars_single_dict():
    input_data = {'key': 'value'}
    expected_output = [{'key': 'value'}]
    result = preprocess_vars(input_data)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_preprocess_vars_list_of_dicts():
    input_data = [{'key1': 'value1'}, {'key2': 'value2'}]
    expected_output = [{'key1': 'value1'}, {'key2': 'value2'}]
    result = preprocess_vars(input_data)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_preprocess_vars_invalid_type():
    input_data = 'not a valid type'
    with pytest.raises(AnsibleError):
        preprocess_vars(input_data)
