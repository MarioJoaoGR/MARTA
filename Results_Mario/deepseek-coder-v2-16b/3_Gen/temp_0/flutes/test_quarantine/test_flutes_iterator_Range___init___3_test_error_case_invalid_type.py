
import pytest
from your_module_name import Range  # Replace 'your_module_name' with the actual module name where Range is defined

def test_error_case_invalid_type():
    with pytest.raises(TypeError):
        r = Range('a', 'b', 'c')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_Range___init___3_test_error_case_invalid_type
flutes/Test4DT_tests/test_flutes_iterator_Range___init___3_test_error_case_invalid_type.py:3:0: E0401: Unable to import 'your_module_name' (import-error)


"""