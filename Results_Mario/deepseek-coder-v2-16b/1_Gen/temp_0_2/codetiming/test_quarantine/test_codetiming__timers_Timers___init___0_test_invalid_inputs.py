
import pytest
from codetiming import Timers

def test_invalid_inputs():
    # Test initializing Timers with invalid name type (non-string)
    with pytest.raises(TypeError):
        Timers(name=123, text='Timing started:', initial_text='Starting...')
    
    # Test initializing Timers with invalid text type (non-string)
    with pytest.raises(TypeError):
        Timers(name='invalid_type', text=None, initial_text='Starting...')
    
    # Test initializing Timers with invalid initial_text type (non-string)
    with pytest.raises(TypeError):
        Timers(name='invalid_type', text='Timing started:', initial_text=123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_codetiming__timers_Timers___init___0_test_invalid_inputs
codetiming/Test4DT_tests/test_codetiming__timers_Timers___init___0_test_invalid_inputs.py:3:0: E0611: No name 'Timers' in module 'codetiming' (no-name-in-module)


"""