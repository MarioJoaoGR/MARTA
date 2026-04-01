
import pytest
from codetiming import Timers
import math
import statistics

def test_valid_input():
    timers = Timers()
    timers['example_timer'] = [1.2, 3.4, 5.6]
    
    assert math.isnan(timers.stdev('example_timer'))
    
    timers['example_timer'].append(7.8)
    assert pytest.approx(timers.stdev('example_timer'), abs=0.1) == 3.499

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_stdev_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)

"""