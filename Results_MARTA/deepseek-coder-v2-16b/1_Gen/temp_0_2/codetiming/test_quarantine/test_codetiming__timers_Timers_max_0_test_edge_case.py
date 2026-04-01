
import pytest
from codetiming import Timers

def test_max():
    timers = Timers()
    timers._timings['test'] = [1, 2, 3]
    assert timers.max('test') == 3

def test_max_empty():
    timers = Timers()
    assert timers.max('nonexistent') == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_max_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_max_0_test_edge_case.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""