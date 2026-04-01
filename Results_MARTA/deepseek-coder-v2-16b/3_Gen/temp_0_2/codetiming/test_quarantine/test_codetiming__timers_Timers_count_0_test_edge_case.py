
from codetiming import Timers
import pytest

def test_count():
    timers = Timers()
    assert timers.count("non_existent_timer") == 0

    # Add a timer entry to check if count reflects it correctly
    timers._timings["test_timer"] = [1.0, 2.0, 3.0]
    assert timers.count("test_timer") == len(timers._timings["test_timer"])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_count_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_count_0_test_edge_case.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""