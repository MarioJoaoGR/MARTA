
import pytest
from codetiming import Timers
import statistics

def test_valid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median("non_existent_timer")
    
    # Adding a valid timer and checking the median
    timers._timings["example_timer"].append(1.0)
    assert timers.median("example_timer") == 1.0
    
    # Adding more timings to check if the median is correctly calculated
    timers._timings["example_timer"].extend([2.0, 3.0])
    assert timers.median("example_timer") == 2.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_median_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_median_0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""