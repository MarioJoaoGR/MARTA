
import pytest
from codetiming import Timers
import statistics

def test_valid_input():
    timers = Timers()
    
    # Adding some timings to the timers dictionary
    timers._timings['example_timer'].extend([1.0, 2.0, 3.0, 4.0, 5.0])
    
    # Calculating the mean for 'example_timer'
    result = timers.mean('example_timer')
    
    # Expected mean value
    expected_mean = statistics.mean([1.0, 2.0, 3.0, 4.0, 5.0])
    
    # Asserting that the calculated mean matches the expected mean
    assert result == expected_mean

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_mean_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_mean_0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)

"""