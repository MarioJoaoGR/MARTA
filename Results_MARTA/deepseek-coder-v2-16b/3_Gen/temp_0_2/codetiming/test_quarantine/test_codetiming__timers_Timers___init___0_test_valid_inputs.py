
import pytest
from codetiming import Timers
from collections import defaultdict, List
from typing import Any, Dict

def test_valid_inputs():
    timers = Timers()
    assert isinstance(timers._timings, defaultdict)
    assert all(isinstance(value, list) for value in timers._timings.values())

    timers_with_args = Timers(arg1='value1', arg2=42)
    assert isinstance(timers_with_args._timings, defaultdict)
    assert all(isinstance(value, list) for value in timers_with_args._timings.values())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers___init___0_test_valid_inputs
codetiming/Test4DT_tests/test_codetiming__timers_Timers___init___0_test_valid_inputs.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)
codetiming/Test4DT_tests/test_codetiming__timers_Timers___init___0_test_valid_inputs.py:4:0: E0611: No name 'List' in module 'collections' (no-name-in-module)


"""