
import pytest
from sty import primitive

def test_error_case():
    with pytest.raises(TypeError):  # Since __init__ does not take any parameters, we expect a TypeError if called with arguments
        Register()  # This should raise an error because the constructor is defined incorrectly

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_primitive_Register___init___2_test_error_case
sty/Test4DT_tests/test_sty_primitive_Register___init___2_test_error_case.py:7:8: E0602: Undefined variable 'Register' (undefined-variable)


"""