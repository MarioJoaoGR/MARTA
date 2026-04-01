
import pytest
from collections import Counter
from dataclasses_json.utils import _get_type_origin, _issubclass_safe

# Define a class that is not a subclass of Counter
class NotACounter(object):
    pass

def test_valid_case_same_type():
    # Create an instance of NotACounter
    not_a_counter = NotACounter()
    
    # Check if the type of not_a_counter is a subclass of Counter
    assert _is_counter(NotACounter) == False, "Expected _is_counter to return False for a non-subclass type"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_counter_1_test_valid_case_same_type
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_1_test_valid_case_same_type.py:15:11: E0602: Undefined variable '_is_counter' (undefined-variable)

"""