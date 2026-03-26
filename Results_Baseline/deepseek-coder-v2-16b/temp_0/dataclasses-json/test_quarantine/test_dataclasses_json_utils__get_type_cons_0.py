
# Module: dataclasses_json.utils
import pytest
from typing import List, Dict
import sys
from dataclasses_json.utils import _get_type_cons

# Test cases for _get_type_cons function

def test_get_type_cons_builtin():
    my_list = [1, 2, 3]
    cons = _get_type_cons(my_list.__class__)
    assert cons == list

def test_get_type_cons_custom():
    class MyCustomType:
        pass
    
    cons = _get_type_cons(MyCustomType)
    assert cons == MyCustomType

def test_get_type_cons_typing():
    from typing import List, Dict
    my_list = [1, 2, 3]
    cons = _get_type_cons(my_list.__class__)
    if sys.version_info >= (3, 7):
        assert cons == list
    else:
        assert cons == MyCustomType
    
    my_dict = {}
    cons = _get_type_cons(my_dict.__class__)
    if sys.version_info >= (3, 7):
        assert cons == dict
    else:
        assert cons == MyCustomType

def test_get_type_cons_invalid():
    with pytest.raises(TypeError):
        _get_type_cons("not a type")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_cons_0
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0.py:29:23: E0602: Undefined variable 'MyCustomType' (undefined-variable)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0.py:36:23: E0602: Undefined variable 'MyCustomType' (undefined-variable)

"""