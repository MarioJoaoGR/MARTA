
import pytest
from typing import Tuple, List
from your_module_name.utils import _get_type_origin, _issubclass_safe  # Replace 'your_module_name' with the actual module name

def test_valid_case_happy_path():
    from typing import Tuple
    
    class MyTuple(Tuple[int, str]):
        pass
    
    assert _is_tuple(MyTuple) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_tuple_0_test_valid_case_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_tuple_0_test_valid_case_happy_path.py:4:0: E0401: Unable to import 'your_module_name.utils' (import-error)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_tuple_0_test_valid_case_happy_path.py:12:11: E0602: Undefined variable '_is_tuple' (undefined-variable)


"""