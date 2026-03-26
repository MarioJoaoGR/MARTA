
from codetiming import Timers
import pytest

def test_invalid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.count("non_existent_timer")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_count_0_test_invalid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_count_0_test_invalid_input.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""