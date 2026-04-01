
import pytest
from codetiming import Timers

def test_valid_inputs():
    timers = Timers()
    with pytest.raises(TypeError) as excinfo:
        timers['timer1'] = 1.0
    assert str(excinfo.value) == "Timers does not support item assignment."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers___setitem___0_test_valid_inputs
codetiming/Test4DT_tests/test_codetiming__timers_Timers___setitem___0_test_valid_inputs.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""