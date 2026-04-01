
import pytest
from collections import Counter

class NotACounter: pass

def test_invalid_input():
    with pytest.raises(TypeError):
        _is_counter(NotACounter)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_counter_1_test_invalid_input
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_1_test_invalid_input.py:9:8: E0602: Undefined variable '_is_counter' (undefined-variable)


"""