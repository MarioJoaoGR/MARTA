
from sty import primitive
import pytest

def test_invalid_inputs():
    # Test that Register cannot be instantiated with unexpected keyword arguments
    with pytest.raises(TypeError):
        Register(renderfuncs=None, is_muted=True, eightbit_call=lambda x: x, rgb_call=lambda r, g, b: (r, g, b))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register___init___2_test_invalid_inputs
sty/Test4DT_tests/test_sty_primitive_Register___init___2_test_invalid_inputs.py:8:8: E0602: Undefined variable 'Register' (undefined-variable)


"""