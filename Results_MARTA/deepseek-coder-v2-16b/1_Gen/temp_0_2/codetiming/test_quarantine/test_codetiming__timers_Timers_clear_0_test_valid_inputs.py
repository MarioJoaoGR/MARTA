
from codetiming import Timers
import pytest

def test_clear():
    timers = Timers()
    timers.start("task1")
    timers.stop("task1")
    assert len(timers._timings) == 1
    
    timers.clear()
    assert len(timers._timings) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_clear_0_test_valid_inputs
codetiming/Test4DT_tests/test_codetiming__timers_Timers_clear_0_test_valid_inputs.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""