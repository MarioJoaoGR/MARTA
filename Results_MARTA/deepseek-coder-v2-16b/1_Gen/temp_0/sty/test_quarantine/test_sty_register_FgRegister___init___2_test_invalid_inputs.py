
import pytest
from sty import register

def test_invalid_inputs():
    with pytest.raises(TypeError):
        FgRegister()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_FgRegister___init___2_test_invalid_inputs
sty/Test4DT_tests/test_sty_register_FgRegister___init___2_test_invalid_inputs.py:7:8: E0602: Undefined variable 'FgRegister' (undefined-variable)

"""