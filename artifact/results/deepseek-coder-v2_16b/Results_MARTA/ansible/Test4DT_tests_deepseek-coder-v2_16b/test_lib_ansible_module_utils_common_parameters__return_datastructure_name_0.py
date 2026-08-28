
import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name
from collections import Mapping, text_type, binary_type

def test_valid_case_dict():
    obj = {'sensitive': 'data', 'otherkey': 123}
    result = list(_return_datastructure_name(obj))
    assert set(result) == {'data', 'otherkey'}

def test_error_case_none():
    with pytest.raises(TypeError) as e:
        obj = None
        result = list(_return_datastructure_name(obj))
    assert str(e.value) == "Unknown parameter type: <class 'NoneType'>"

def test_error_case_invalid_type():
    with pytest.raises(TypeError) as e:
        obj = 123
        result = list(_return_datastructure_name(obj))
    assert str(e.value) == "Unknown parameter type: <class 'int'>"
