
from codetiming import Timers
import pytest
from collections import defaultdict

def test_init():
    timers = Timers()
    assert isinstance(timers._timings, defaultdict)
    assert type(timers._timings['default']) == list
    assert len(timers._timings['default']) == 0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers___init___0_test_edge_cases
codetiming/Test4DT_tests/test_codetiming__timers_Timers___init___0_test_edge_cases.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""