
import pytest
from sty.primitive import Style
from unittest.mock import patch

@pytest.fixture
def register():
    return Register()

def test_mute(register):
    # Initial state check
    assert not register.is_muted
    
    # Muting the register
    register.mute()
    
    # Check if the register is muted
    assert register.is_muted
    
    # Check if other attributes are reset to their default values (if they are instances of Style)
    for attr_name in dir(register):
        val = getattr(register, attr_name)
        if isinstance(val, Style):
            with patch.object(Style, '__init__', return_value=None):
                assert getattr(register, attr_name) == Style()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_mute_3_test_valid_input
sty/Test4DT_tests/test_sty_primitive_Register_mute_3_test_valid_input.py:8:11: E0602: Undefined variable 'Register' (undefined-variable)


"""