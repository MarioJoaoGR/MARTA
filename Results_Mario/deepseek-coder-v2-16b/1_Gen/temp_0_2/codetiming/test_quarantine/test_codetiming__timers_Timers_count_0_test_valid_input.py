
from codetiming import Timers
import pytest

def test_count_valid_input():
    timers = Timers()
    timers._timings['test'] = [1.0, 2.0, 3.0]
    assert timers.count('test') == 3.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_count_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_count_0_test_valid_input.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""