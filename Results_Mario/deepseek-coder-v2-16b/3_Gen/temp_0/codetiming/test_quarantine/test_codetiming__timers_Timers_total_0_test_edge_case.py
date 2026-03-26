
from codetiming import Timers
import pytest
from collections import defaultdict

def test_timers_initialization():
    timers = Timers()
    assert isinstance(timers._timings, defaultdict)
    assert isinstance(timers._timings, dict)  # Ensure it's a dictionary and not just a defaultdict

def test_total_method():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.total('non_existent_timer')
    
    timers._timings['test_timer'].append(1.0)
    assert timers.total('test_timer') == 1.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_total_0_test_edge_case
codetiming/Test4DT_tests/test_codetiming__timers_Timers_total_0_test_edge_case.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""