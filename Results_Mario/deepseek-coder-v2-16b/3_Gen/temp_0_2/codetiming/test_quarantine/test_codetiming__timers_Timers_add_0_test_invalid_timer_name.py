
import pytest
from codetiming import Timers

def test_invalid_timer_name():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.add('non_existent_timer', 1.0)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0_test_invalid_timer_name
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_invalid_timer_name.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""