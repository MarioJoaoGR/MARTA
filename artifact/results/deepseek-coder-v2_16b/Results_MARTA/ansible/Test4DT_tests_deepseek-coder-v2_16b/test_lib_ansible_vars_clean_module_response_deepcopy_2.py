
import pytest
from ansible.vars.clean import module_response_deepcopy

def test_valid_input_dictionary():
    original_dict = {'a': 1, 'b': {'c': 2}}
    copied_dict = module_response_deepcopy(original_dict)
    assert isinstance(copied_dict, dict), "Copied object is not a dictionary"
    assert copied_dict == original_dict, "Deep copy failed"
    original_dict['b']['c'] = 3
    assert copied_dict['b']['c'] == 2, "Modification of original should not affect the copy"

def test_valid_input_list():
    original_list = [1, {'a': 2}]
    copied_list = module_response_deepcopy(original_list)
    assert isinstance(copied_list, list), "Copied object is not a list"
    assert copied_list == original_list, "Deep copy failed"
    original_list[1]['a'] = 3
    assert copied_list[1]['a'] == 2, "Modification of original should not affect the copy"

def test_invalid_input():
    non_copyable = "not a dict or list"
    result = module_response_deepcopy(non_copyable)
    assert result == non_copyable, "Non-copyable input should be returned unchanged"
