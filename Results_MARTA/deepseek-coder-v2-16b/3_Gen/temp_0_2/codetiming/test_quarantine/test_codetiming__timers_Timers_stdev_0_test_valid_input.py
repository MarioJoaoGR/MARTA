
import pytest
from codetiming import Timers
import math
import statistics

def test_valid_input():
    timers = Timers()
    
    # Adding some timings for a specific name
    timers._timings['test'].extend([1.0, 2.0, 3.0])
    
    # Calculating standard deviation
    result = timers.stdev('test')
    
    # Expected standard deviation is the actual stdev of [1.0, 2.0, 3.0] which is approximately 1.0
    assert math.isclose(result, 1.0)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_stdev_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""