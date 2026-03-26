
import pytest
from codetiming import Timers
import statistics

def test_mean():
    timers = Timers()
    timers._timings['test'] = [1, 2, 3]
    assert timers.mean('test') == statistics.mean([1, 2, 3])

def test_mean_empty():
    timers = Timers()
    assert timers.mean('nonexistent') == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_mean_0_test_error_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_mean_0_test_error_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""