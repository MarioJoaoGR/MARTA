
# Module: string_utils.validation
import pytest
from string_utils.validation import is_number
from re import match

# Assuming the regex pattern for number validation is defined elsewhere in the module
NUMBER_RE = r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$"

def test_valid_integer():
    assert is_number('42') == True

def test_valid_floating_point():
    assert is_number('19.99') == True

def test_valid_scientific_notation():
    assert is_number('1e3') == True

def test_invalid_string_with_spaces():
    assert is_number('1 2 3') == False

def test_non_string_input():
    from string_utils.exceptions import InvalidInputError
    with pytest.raises(InvalidInputError):
        is_number(12345)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_validation_is_number_0
python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_0.py:23:4: E0401: Unable to import 'string_utils.exceptions' (import-error)
python-string-utils/Test4DT_tests/test_string_utils_validation_is_number_0.py:23:4: E0611: No name 'exceptions' in module 'string_utils' (no-name-in-module)

"""