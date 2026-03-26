
from codetiming import Timers
import pytest
from typing import List, Callable, Dict
import collections

def test_apply_valid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "example_timer")
    
    # Add a timing to simulate the scenario where the timer exists
    timers._timings["example_timer"].append(1.0)
    assert timers.apply(lambda x: sum(x), "example_timer") == 1.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_apply_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_0_test_valid_input.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""