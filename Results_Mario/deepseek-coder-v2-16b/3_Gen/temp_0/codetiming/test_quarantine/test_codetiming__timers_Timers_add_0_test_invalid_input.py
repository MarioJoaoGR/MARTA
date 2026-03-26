
import pytest
from codetiming import Timers

def test_invalid_input():
    timers = Timers()
    
    # Test adding a negative value to a timer
    with pytest.raises(ValueError):
        timers.add('test_timer', -1)
        
    # Ensure the timing data for 'test_timer' is not added due to invalid input
    assert len(timers._timings['test_timer']) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0_test_invalid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_invalid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""