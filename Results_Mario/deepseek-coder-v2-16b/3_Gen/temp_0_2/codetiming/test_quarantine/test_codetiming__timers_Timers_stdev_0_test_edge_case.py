
import pytest
from codetiming import Timers
import math
import statistics

def test_stdev_with_valid_name():
    timers = Timers()
    timers.start('test')
    # Add some timings to ensure we have enough data for stdev calculation
    timers._timings['test'].extend([10, 20, 30])
    assert math.isnan(timers.stdev('test'))  # Initially should be nan as not enough data
    
    timers._timings['test'].append(40)  # Add one more timing to ensure we have at least two measurements
    assert not math.isnan(timers.stdev('test'))  # Now it should calculate the stdev
    assert pytest.approx(timers.stdev('test'), abs=1e-6) == statistics.stdev([10, 20, 30, 40])

def test_stdev_with_invalid_name():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('nonexistent')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_stdev_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""