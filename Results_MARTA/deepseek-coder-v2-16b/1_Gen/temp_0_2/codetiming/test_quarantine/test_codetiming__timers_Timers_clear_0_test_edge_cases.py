
from codetiming import Timers
import pytest

def test_clear():
    timers = Timers()
    timers.start("task1")
    timers.stop("task1")
    
    # Before clearing, check that there is data in the timings dictionary
    assert "task1" in timers._timings
    assert len(timers._timings["task1"]) == 2  # Should have start and stop times
    
    # Clear the timers
    timers.clear()
    
    # After clearing, check that the data has been removed from the timings dictionary
    assert "task1" not in timers._timings
    assert len(timers._timings) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_clear_0_test_edge_cases
codetiming/Test4DT_tests/test_codetiming__timers_Timers_clear_0_test_edge_cases.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""