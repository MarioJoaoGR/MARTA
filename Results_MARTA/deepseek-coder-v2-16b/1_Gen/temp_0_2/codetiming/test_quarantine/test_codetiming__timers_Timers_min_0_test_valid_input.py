
import pytest
from codetiming import Timers

def test_min_valid_input():
    timers = Timers()
    timers._timings['operation1'] = [0.1, 0.2, 0.3]
    
    result = timers.min('operation1')
    assert result == 0.1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_min_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_min_0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""