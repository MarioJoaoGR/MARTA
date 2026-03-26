
import pytest
from string_utils.validation import is_full_string

def test_empty_string():
    input_string = ''
    assert not is_isogram(input_string), "Expected False for an empty string"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_isogram_2_test_empty_string
python-string-utils/Test4DT_tests/test_string_utils_validation_is_isogram_2_test_empty_string.py:7:15: E0602: Undefined variable 'is_isogram' (undefined-variable)


"""