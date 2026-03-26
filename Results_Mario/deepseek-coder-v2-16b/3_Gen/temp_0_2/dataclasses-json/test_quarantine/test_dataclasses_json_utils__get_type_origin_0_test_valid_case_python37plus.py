
import sys
from dataclasses_json.utils import _get_type_origin, _NO_TYPE_ORIGIN
from typing import List, Union

def test_valid_case_python37plus():
    # Test for Python 3.7 and later where __origin__ is used directly
    my_list = List[int]
    assert isinstance(my_list, list)
    assert _get_type_origin(my_list) == list
    
    from collections import deque
    class MyDeque(deque): pass
    my_deque = MyDeque()  # Assuming MyDeque is a subclass of deque
    assert isinstance(my_deque, deque)
    assert _get_type_origin(my_deque) == deque
    
    # Test for Python 3.6 where __extra__ might be used if __origin__ is None or not present
    from typing import Optional
    class MyOptional(Union): pass  # Union is a type in Python 3.7+ but here we mock it as a class
    my_optional = MyOptional[int]
    assert isinstance(my_optional, int)
    assert _get_type_origin(my_optional) == int
    
    # Test for cases where the origin cannot be determined (e.g., custom types)
    class CustomType: pass
    assert _get_type_origin(CustomType) is None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_origin_0_test_valid_case_python37plus
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_case_python37plus.py:20:4: E0239: Inheriting 'Union', which is not a class. (inherit-non-class)


"""