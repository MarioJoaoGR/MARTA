
import pytest
from sty.primitive import Style  # Importing Style from the correct module
from sty.Test4DT_tests.test_sty_primitive_Register_mute_3_test_edge_case import Register  # Adjust the import path as necessary

def test_mute():
    reg = Register()
    assert not reg.is_muted, "Initial state should be unmuted"
    
    reg.mute()
    assert reg.is_muted, "After calling mute(), is_muted should be True"
    
    # Check that all attributes of type Style are also muted
    for attr_name in dir(reg):
        val = getattr(reg, attr_name)
        if isinstance(val, Style):
            assert val.is_muted == True, f"{attr_name} should be muted"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_mute_3_test_edge_case
sty/Test4DT_tests/test_sty_primitive_Register_mute_3_test_edge_case.py:4:0: E0401: Unable to import 'sty.Test4DT_tests.test_sty_primitive_Register_mute_3_test_edge_case' (import-error)
sty/Test4DT_tests/test_sty_primitive_Register_mute_3_test_edge_case.py:4:0: E0611: No name 'Test4DT_tests' in module 'sty' (no-name-in-module)


"""