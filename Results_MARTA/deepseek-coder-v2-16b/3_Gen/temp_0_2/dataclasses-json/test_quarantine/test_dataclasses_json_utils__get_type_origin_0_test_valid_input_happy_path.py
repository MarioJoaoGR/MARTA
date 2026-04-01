
import pytest
from dataclasses_json.utils import _get_type_origin, List, deque, MyDeque

def test_valid_input_happy_path():
    # Test with a standard type from the typing module
    my_list = List[int]
    assert _get_type_origin(my_list) == list
    
    # Test with a custom class that is not derived from any specific base
    class MyDeque: pass
    my_deque = MyDeque()  # Assuming MyDeque is a subclass of deque
    assert _get_type_origin(my_deque) == deque

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__get_type_origin_0_test_valid_input_happy_path
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input_happy_path.py:3:0: E0611: No name 'List' in module 'dataclasses_json.utils' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input_happy_path.py:3:0: E0611: No name 'deque' in module 'dataclasses_json.utils' (no-name-in-module)
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_origin_0_test_valid_input_happy_path.py:3:0: E0611: No name 'MyDeque' in module 'dataclasses_json.utils' (no-name-in-module)


"""