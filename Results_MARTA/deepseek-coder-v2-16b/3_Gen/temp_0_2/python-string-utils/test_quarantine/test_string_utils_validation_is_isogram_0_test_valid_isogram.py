
import pytest
from string_utils.validation import is_full_string

def test_valid_isogram():
    input_string = 'dermatoglyphics'
    assert is_isogram(input_string) == True, f"Expected True for '{input_string}', but got False"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_isogram_0_test_valid_isogram
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_0_test_valid_isogram.py:7:11: E0602: Undefined variable 'is_isogram' (undefined-variable)


"""