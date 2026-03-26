
import pytest
from flutes.multiproc import get_arg

def test_invalid_inputs():
    # Test when pos is out of range
    with pytest.raises(IndexError):
        get_arg(pos=10, name='non_existent', default='default_value')
    
    # Test when name is not in kwargs and no default is provided
    assert get_arg(pos=0, name='non_existent') == None
    
    # Test with valid inputs
    assert get_arg(pos=0, name='name', default='default_value') == 'default_value'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_get_arg_0_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_multiproc_get_arg_0_test_invalid_inputs.py:3:0: E0611: No name 'get_arg' in module 'flutes.multiproc' (no-name-in-module)


"""