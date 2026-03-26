
import pytest
from codetiming import Timers
import statistics

def test_median():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.median("non_existent_timer")
    
    # Test median with no timings
    assert timers.median("test_timer") == 0
    
    # Add some timings
    timers._timings["test_timer"].extend([1, 2, 3, 4, 5])
    assert timers.median("test_timer") == 3
    
    # Test median with an even number of timings
    timers._timings["test_timer"].extend([6, 7])
    assert timers.median("test_timer") == 4.5

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_median_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_median_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""