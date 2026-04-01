
from sty.primitive import Style  # Importing Style from the correct module
import pytest

def test_mute():
    reg = Register()  # Create an instance of Register
    assert not reg.is_muted  # Assert that the register is initially not muted
    
    reg.mute()  # Call the mute method to mute the register
    assert reg.is_muted  # Assert that the register is now muted
    
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, Style):
            assert val.mute()  # Ensure all attributes of type Style are also muted

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_mute_1_test_edge_case
sty/Test4DT_tests/test_sty_primitive_Register_mute_1_test_edge_case.py:6:10: E0602: Undefined variable 'Register' (undefined-variable)


"""