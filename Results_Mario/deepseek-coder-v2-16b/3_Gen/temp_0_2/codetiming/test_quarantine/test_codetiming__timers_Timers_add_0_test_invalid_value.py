
from codetiming import Timers
import pytest

def test_invalid_value():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.add('test', 'not_a_float')  # This should raise a KeyError because the value is not a float

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0_test_invalid_value
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_invalid_value.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""