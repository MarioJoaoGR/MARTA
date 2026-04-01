
import pytest
from string_utils.manipulation import __StringCompressor
from custom_exceptions import InvalidInputError

def test_value_error_for_empty_string():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.__require_valid_input_and_encoding("", "utf-8")
    assert str(excinfo.value) == 'Input string cannot be empty'

def test_invalid_encoding_type():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.__require_valid_input_and_encoding("example", 123)
    assert str(excinfo.value) == 'Invalid encoding'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_value_error_for_empty_string
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_value_error_for_empty_string.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""