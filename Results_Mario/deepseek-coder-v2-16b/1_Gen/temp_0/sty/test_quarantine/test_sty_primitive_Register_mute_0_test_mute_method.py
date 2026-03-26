
from sty import Style, fg, bg, ef, rs
from unittest.mock import MagicMock
import pytest

@pytest.fixture
def register():
    reg = Register()
    return reg

def test_mute_method(register):
    # Ensure the register is not muted initially
    assert not register.is_muted
    
    # Mute the register
    register.mute()
    
    # Check that the register is now muted
    assert register.is_muted
    
    # Check that all style attributes are reset to their default values
    for attr_name in dir(register):
        val = getattr(register, attr_name)
        if isinstance(val, Style):
            assert val == Style()  # Assuming Style has a method to return default values or can be instantiated without arguments

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_mute_0_test_mute_method
sty/Test4DT_tests/test_sty_primitive_Register_mute_0_test_mute_method.py:8:10: E0602: Undefined variable 'Register' (undefined-variable)

"""