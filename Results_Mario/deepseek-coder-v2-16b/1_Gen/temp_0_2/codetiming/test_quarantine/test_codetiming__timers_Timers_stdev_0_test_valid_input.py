
import pytest
from codetiming import Timers
import math
import statistics

def test_valid_input():
    timers = Timers()
    timers._timings['example'] = [10, 20, 30]
    
    assert math.isnan(timers.stdev('nonexistent')) is True
    assert pytest.approx(timers.stdev('example'), abs=0.01) == 8.165

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_stdev_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""