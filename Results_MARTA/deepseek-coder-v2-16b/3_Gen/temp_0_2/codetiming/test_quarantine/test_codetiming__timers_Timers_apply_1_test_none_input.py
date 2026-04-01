
from codetiming import Timers
import pytest
from typing import List, Callable, Dict

def test_none_input():
    timers = Timers()
    with pytest.raises(KeyError):
        result = timers.apply(lambda x: sum(x), "operation1")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_apply_1_test_none_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_1_test_none_input.py:2:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""