
from codetiming import Timers
import pytest
from typing import List, Callable, Dict
import collections

@pytest.fixture
def timers():
    return Timers()

def test_apply_with_empty_timings(timers):
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "operation1")

def test_apply_with_existing_timing(timers):
    timers._timings["operation1"].append(1.0)
    result = timers.apply(lambda x: sum(x), "operation1")
    assert result == 1.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_apply_1_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_1_test_edge_case.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""