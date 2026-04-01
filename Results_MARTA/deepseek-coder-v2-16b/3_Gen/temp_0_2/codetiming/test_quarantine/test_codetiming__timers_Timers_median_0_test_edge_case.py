
import pytest
from codetiming import Timers
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_median_empty(timers):
    with pytest.raises(KeyError):
        timers.median("non_existent_timer")

def test_median_single_value(timers):
    timers._timings["test_timer"].append(1.0)
    assert timers.median("test_timer") == 1.0

def test_median_multiple_values(timers):
    timers._timings["test_timer"].extend([1.0, 2.0, 3.0])
    assert timers.median("test_timer") == 2.0

def test_median_zero_values(timers):
    timers._timings["test_timer"].extend([0.0, 0.0, 0.0])
    assert timers.median("test_timer") == 0.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_median_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_median_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""