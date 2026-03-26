
import pytest
from sty import register

class TestFgRegister:
    def test_error_case(self):
        with pytest.raises(ValueError):
            FgRegister()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_sty_register_FgRegister___init___1_test_error_case
sty/Test4DT_tests/test_sty_register_FgRegister___init___1_test_error_case.py:8:12: E0602: Undefined variable 'FgRegister' (undefined-variable)


"""