
from codetiming import Timers
import pytest

def test_valid_case():
    timers = Timers()
    assert isinstance(timers._timings, dict)
    assert len(timers._timings) == 0
    
    timers.add("test_timer", 1.23)
    assert "test_timer" in timers._timings
    assert len(timers._timings["test_timer"]) == 1
    assert timers._timings["test_timer"][0] == 1.23
    
    timers.add("test_timer", 4.56)
    assert len(timers._timings["test_timer"]) == 2
    assert timers._timings["test_timer"] == [1.23, 4.56]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0_test_valid_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_valid_case.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""