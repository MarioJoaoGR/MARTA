
import pytest
from codetiming import Timers

def test_min():
    timers = Timers()
    assert timers.min("non_existent_name") == 0
    
    timers._timings["test"].append(1.0)
    timers._timings["test"].append(2.0)
    timers._timings["test"].append(3.0)
    
    assert timers.min("test") == 1.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_min_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_min_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""