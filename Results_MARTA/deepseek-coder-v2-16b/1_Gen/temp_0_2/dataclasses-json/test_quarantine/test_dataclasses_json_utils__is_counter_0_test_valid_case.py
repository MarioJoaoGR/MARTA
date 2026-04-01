
import pytest
from collections import Counter

class MyCounter(Counter[str]): pass

def test_valid_case():
    assert _is_counter(MyCounter) == True

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_counter_0_test_valid_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_0_test_valid_case.py:8:11: E0602: Undefined variable '_is_counter' (undefined-variable)


"""