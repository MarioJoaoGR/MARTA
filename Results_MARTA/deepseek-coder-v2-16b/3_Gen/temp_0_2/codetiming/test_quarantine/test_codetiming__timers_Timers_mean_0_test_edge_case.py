
import pytest
from codetiming import Timers
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_mean_empty(timers):
    with pytest.raises(KeyError):
        timers.mean("operation1")

def test_mean_one_value(timers):
    timers._timings["operation1"].append(1.0)
    assert timers.mean("operation1") == 1.0

def test_mean_multiple_values(timers):
    timers._timings["operation1"].extend([1.0, 2.0, 3.0])
    assert timers.mean("operation1") == statistics.mean([1.0, 2.0, 3.0])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_mean_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_mean_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""