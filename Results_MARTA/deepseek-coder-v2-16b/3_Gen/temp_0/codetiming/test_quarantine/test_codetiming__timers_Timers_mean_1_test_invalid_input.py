
import pytest
from codetiming import Timers
import statistics

def test_invalid_input():
    timers = Timers()
    
    # Test mean method with an uninitialized timer name
    with pytest.raises(KeyError):
        timers.mean("uninitialized_timer")
        
    # Test apply method with an uninitialized timer name
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "uninitialized_timer")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_mean_1_test_invalid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_mean_1_test_invalid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""