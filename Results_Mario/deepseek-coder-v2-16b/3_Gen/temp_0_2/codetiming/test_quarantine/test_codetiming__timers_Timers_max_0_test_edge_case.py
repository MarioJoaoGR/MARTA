
import pytest
from codetiming import Timers

def test_max():
    timers = Timers()
    assert timers.max("non_existent_timer") == 0
    
    timers._timings["test_timer"].append(1.0)
    assert timers.max("test_timer") == 1.0
    
    timers._timings["test_timer"].extend([2.0, 3.0])
    assert timers.max("test_timer") == 3.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_max_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_max_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""