
import pytest
from collections import Counter

class MyCounter(Counter):
    pass

def test_valid_case_subclass():
    my_counter = MyCounter()
    assert _is_counter(MyCounter) == True, "Expected MyCounter to be recognized as a subclass of Counter"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_counter_0_test_valid_case_subclass
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_0_test_valid_case_subclass.py:10:11: E0602: Undefined variable '_is_counter' (undefined-variable)

"""