
import pytest
from codetiming import Timers

def test_valid_input():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.apply(lambda x: sum(x), "operation1")
    
    timers._timings["operation1"].append(1.0)
    assert timers.apply(lambda x: sum(x), "operation1") == 1.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_apply_1_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_apply_1_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""