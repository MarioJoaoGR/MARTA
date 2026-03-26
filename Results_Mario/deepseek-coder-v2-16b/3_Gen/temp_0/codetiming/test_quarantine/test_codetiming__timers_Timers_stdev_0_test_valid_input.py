
import pytest
from codetiming import Timers
import math
import statistics

def test_valid_input():
    timers = Timers()
    timers['example_timer'] = [1.2, 3.4, 5.6]
    
    assert isinstance(timers._timings, dict)
    assert 'example_timer' in timers._timings
    assert len(timers._timings['example_timer']) == 3
    
    stdev = timers.stdev('example_timer')
    assert math.isnan(stdev) == False
    assert pytest.approx(stdev, abs=0.1) == statistics.stdev([1.2, 3.4, 5.6])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_stdev_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""