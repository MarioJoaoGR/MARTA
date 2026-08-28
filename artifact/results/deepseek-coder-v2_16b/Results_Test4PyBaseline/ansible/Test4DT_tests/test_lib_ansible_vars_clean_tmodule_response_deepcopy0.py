
import pytest
from ansible.vars.clean import module_response_deepcopy
import copy
import six

# Test deep copying a dictionary
def test_module_response_deepcopy_dict():
    original_dict = {'key1': 'value1', 'key2': [1, 2, 3]}
    copied_dict = module_response_deepcopy(original_dict)
    assert copied_dict == original_dict
    assert copied_dict is not original_dict

# Test deep copying a list
def test_module_response_deepcopy_list():
    original_list = [{'subkey1': 'subvalue1'}, {'subkey2': 'subvalue2'}]
    copied_list = module_response_deepcopy(original_list)
    assert copied_list == original_list