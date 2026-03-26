
import pytest
from superstring.superstring import SuperStringUpper

def test_edge_case_none():
    with pytest.raises(TypeError):
        str_upper = SuperStringUpper()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_superstring_superstring_SuperStringUpper_lower_0_test_edge_case_none
superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_lower_0_test_edge_case_none.py:7:20: E1120: No value for argument 'base' in constructor call (no-value-for-parameter)


"""