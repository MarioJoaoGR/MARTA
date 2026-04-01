
import pytest
from codetiming import Timers

def test_clear():
    timers = Timers()
    timers['timer1'] = [1.0, 2.0, 3.0]
    assert len(timers) == 1
    assert 'timer1' in timers
    
    timers.clear()
    assert len(timers) == 0
    assert 'timer1' not in timers

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_clear_0_test_edge_cases
codetiming/Test4DT_tests/test_codetiming__timers_Timers_clear_0_test_edge_cases.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""