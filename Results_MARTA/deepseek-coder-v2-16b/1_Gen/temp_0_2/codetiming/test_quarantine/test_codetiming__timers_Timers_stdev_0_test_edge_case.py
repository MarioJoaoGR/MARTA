
import pytest
from codetiming import Timers
import math
import statistics

@pytest.fixture
def timers():
    return Timers()

def test_stdev_with_valid_name(timers):
    timers._timings['example'] = [10, 20, 30]
    assert math.isclose(timers.stdev('example'), 8.165, rel_tol=1e-3)

def test_stdev_with_invalid_name(timers):
    with pytest.raises(KeyError):
        timers.stdev('nonexistent')

def test_stdev_with_less_than_two_entries(timers):
    timers._timings['test'] = [10]
    assert math.isnan(timers.stdev('test'))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_stdev_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_stdev_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""