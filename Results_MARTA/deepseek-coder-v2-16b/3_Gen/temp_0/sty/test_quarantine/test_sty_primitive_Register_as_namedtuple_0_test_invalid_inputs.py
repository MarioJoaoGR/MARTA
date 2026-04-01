
import pytest
from sty.primitive import Register

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Attempting to create an instance of Register with invalid inputs should raise a TypeError
        Register("extra", "arguments")  # This should fail because the constructor does not accept positional arguments

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register_as_namedtuple_0_test_invalid_inputs
sty/Test4DT_tests/test_sty_primitive_Register_as_namedtuple_0_test_invalid_inputs.py:8:8: E1121: Too many positional arguments for constructor call (too-many-function-args)


"""