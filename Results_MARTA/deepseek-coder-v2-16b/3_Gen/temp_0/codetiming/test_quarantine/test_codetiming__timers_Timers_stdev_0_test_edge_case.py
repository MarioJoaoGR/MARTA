
import pytest
from codetiming import Timers
import math
import statistics

def test_stdev():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.stdev('non_existent_timer')
    
    timers._timings['test_timer'] = [1, 2, 3, 4]
    assert math.isnan(timers.stdev('test_timer'))
    
    timers._timings['test_timer'].append(5)
    assert pytest.approx(timers.stdev('test_timer'), abs=0.1) == statistics.stdev([1, 2, 3, 4, 5])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_stdev_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""