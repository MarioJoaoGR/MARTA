
import pytest
from codetiming import Timers

def test_edge_case_none():
    timers = Timers()
    assert isinstance(timers._timings, dict)
    assert timers._timings == {}

    # Adding a timing value
    timers.add('test_timer', 1.0)
    assert 'test_timer' in timers._timings
    assert len(timers._timings['test_timer']) == 1
    assert timers._timings['test_timer'][0] == 1.0

    # Adding another timing value
    timers.add('test_timer', 2.0)
    assert len(timers._timings['test_timer']) == 2
    assert timers._timings['test_timer'] == [1.0, 2.0]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_add_0_test_edge_case_none
codetiming/Test4DT_tests/test_codetiming__timers_Timers_add_0_test_edge_case_none.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""