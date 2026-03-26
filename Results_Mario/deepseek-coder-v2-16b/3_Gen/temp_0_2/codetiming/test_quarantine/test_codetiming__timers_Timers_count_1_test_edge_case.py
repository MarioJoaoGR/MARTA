
import pytest
from codetiming import Timers

def test_count():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.count("non_existent_timer")
    
    timers._timings["example_timer"].append(1.0)
    assert timers.count("example_timer") == 1.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_count_1_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_count_1_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""