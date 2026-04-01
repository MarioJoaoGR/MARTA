
from codetiming import Timers
import pytest

def test_valid_input():
    timers = Timers()
    timers.add('test_timer', 1.0)
    
    assert 'test_timer' in timers._timings
    assert len(timers._timings['test_timer']) == 1
    assert timers._timings['test_timer'][0] == 1.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_valid_input.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""