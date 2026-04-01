
import pytest
from codetiming import Timers

def test_valid_inputs():
    timers = Timers()
    assert isinstance(timers._timings, dict)
    assert all(isinstance(value, list) for value in timers._timings.values())
    assert all(isinstance(item, float) for sublist in timers._timings.values() for item in sublist)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers___init___0_test_valid_inputs
codetiming/Test4DT_tests/test_codetiming__timers_Timers___init___0_test_valid_inputs.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)

"""