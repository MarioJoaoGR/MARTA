
import pytest
from codetiming import Timers

def test_invalid_input():
    timers = Timers()
    
    # Test adding a negative value to the timer
    with pytest.raises(ValueError):
        timers.add('test_timer', -1)
    
    # Ensure that no timings are added for invalid inputs
    assert 'test_timer' not in timers._timings
    assert 'test_timer' not in timers.data

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0_test_invalid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_invalid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)

"""