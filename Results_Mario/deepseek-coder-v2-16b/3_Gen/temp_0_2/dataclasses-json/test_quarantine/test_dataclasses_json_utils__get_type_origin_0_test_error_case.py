
import pytest
from dataclasses_json.utils import _get_type_origin, _NO_TYPE_ORIGIN
from typing import List, Union

# Mocking sys.version_info to simulate different Python versions
class MockVersionInfo:
    minor = 6

sys.version_info = MockVersionInfo()

def test_get_type_origin_python36():
    # Test for Python 3.6 where __extra__ is used instead of __origin__
    class MyList(list): pass
    my_list = List[int]
    assert _get_type_origin(my_list) == list
    
    my_union = Union[int, str]
    assert _get_type_origin(my_union) == (int, str)

def test_get_type_origin_python37():
    # Test for Python 3.7 where __origin__ is used directly
    from typing import List
    my_list = List[int]
    assert _get_type_origin(my_list) == list
    
    my_union = Union[int, str]
    assert _get_type_origin(my_union) == (int, str)

def test_get_type_origin_no_origin():
    # Test when the type has no origin
    class MyClass: pass
    assert _get_type_origin(MyClass) == MyClass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_origin_0_test_error_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_error_case.py:10:0: E0602: Undefined variable 'sys' (undefined-variable)


"""