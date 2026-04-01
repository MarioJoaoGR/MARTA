
import pytest
from sty import Register
from sty.primitive import Renderfuncs, Style

def test_invalid_input():
    register = Register()
    with pytest.raises(TypeError):
        register.unmute("extra_argument")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_unmute_8_test_invalid_input
sty/Test4DT_tests/test_sty_primitive_Register_unmute_8_test_invalid_input.py:9:8: E1121: Too many positional arguments for method call (too-many-function-args)


"""