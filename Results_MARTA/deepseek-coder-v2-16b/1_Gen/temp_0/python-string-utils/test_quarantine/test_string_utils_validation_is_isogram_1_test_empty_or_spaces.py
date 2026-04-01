
import pytest
from your_module import is_isogram  # Replace 'your_module' with the actual module name where is_isogram is defined

def test_empty_or_spaces():
    input_string = ' '
    assert not is_isogram(input_string), "Expected False for an empty string or a string with only spaces"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_isogram_1_test_empty_or_spaces
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_1_test_empty_or_spaces.py:3:0: E0401: Unable to import 'your_module' (import-error)

"""