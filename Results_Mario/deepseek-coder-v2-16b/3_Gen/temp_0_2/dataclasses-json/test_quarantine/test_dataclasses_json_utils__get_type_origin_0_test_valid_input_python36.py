
import sys
from typing import _NO_TYPE_ORIGIN, List
from collections import deque

def _get_type_origin(type_):
    """Some spaghetti logic to accommodate differences between 3.6 and 3.7 in
    the typing api"""
    try:
        origin = type_.__origin__
    except AttributeError:
        # Issue #341 and PR #346:
        # For some cases, the type_.__origin__ exists but is set to None
        origin = _NO_TYPE_ORIGIN

    if sys.version_info.minor == 6:
        try:
            origin = type_.__extra__
        except AttributeError:
            origin = type_
        else:
            origin = type_ if origin in (None, _NO_TYPE_ORIGIN) else origin
    elif origin is _NO_TYPE_ORIGIN:
        origin = type_
    return origin

def test_valid_input_python36():
    from collections import deque
    
    class MyDeque(deque): pass
    
    # Test with a standard type
    my_list = List[int]
    assert _get_type_origin(my_list) == list
    
    # Test with a custom subclassed type
    my_deque = MyDeque()  # Assuming MyDeque is a subclass of deque
    assert _get_type_origin(my_deque) == deque

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_origin_0_test_valid_input_python36
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input_python36.py:3:0: E0611: No name '_NO_TYPE_ORIGIN' in module 'typing' (no-name-in-module)


"""