
import pytest
from sty import Register

def test_invalid_input():
    register = Register()
    with pytest.raises(TypeError):  # Since unmute does not take any arguments, we expect a TypeError for invalid input
        register.unmute("extra argument")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_unmute_2_test_invalid_input
sty/Test4DT_tests/test_sty_primitive_Register_unmute_2_test_invalid_input.py:8:8: E1121: Too many positional arguments for method call (too-many-function-args)


"""