
import pytest
from codetiming import Timers
import statistics

def test_mean():
    timers = Timers()
    with pytest.raises(KeyError):
        timers.mean("operation1")
    
    timers._timings["operation1"].append(1.0)
    assert timers.mean("operation1") == 1.0
    
    timers._timings["operation1"].extend([2.0, 3.0])
    assert timers.mean("operation1") == 2.0

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers_mean_0_test_valid_input
codetiming/Test4DT_tests/test_codetiming__timers_Timers_mean_0_test_valid_input.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""