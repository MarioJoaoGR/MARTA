
import pytest
from ansible.plugins.filter.core import dict_to_list_of_dict_key_value_elements, AnsibleFilterTypeError
from collections.abc import Mapping

def test_valid_input():
    mydict = {'a': 1, 'b': 2}
    result = dict_to_list_of_dict_key_value_elements(mydict)
    expected = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}]
    assert result == expected

def test_none_input():
    mydict = None
    with pytest.raises(AnsibleFilterTypeError):
        dict_to_list_of_dict_key_value_elements(mydict)

def test_invalid_type():
    mydict = [1, 2, 3]
    with pytest.raises(AnsibleFilterTypeError):
        dict_to_list_of_dict_key_value_elements(mydict)
