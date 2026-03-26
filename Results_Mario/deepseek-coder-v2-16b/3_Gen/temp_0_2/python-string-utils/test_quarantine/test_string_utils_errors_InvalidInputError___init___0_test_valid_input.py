
import pytest
from your_module_name import InvalidInputError  # Replace with actual module name

def test_valid_input():
    try:
        process_string("valid string")
    except InvalidInputError as e:
        assert False, "Expected no error for valid input"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_errors_InvalidInputError___init___0_test_valid_input
python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0_test_valid_input.py:3:0: E0401: Unable to import 'your_module_name' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_errors_InvalidInputError___init___0_test_valid_input.py:7:8: E0602: Undefined variable 'process_string' (undefined-variable)


"""