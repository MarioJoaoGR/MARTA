
import pytest
from string_utils.manipulation import __StringCompressor
from custom_exceptions import InvalidInputError

def is_string(value):
    return isinstance(value, str)

def test_valid_input_and_encoding_happy_path():
    # Test with valid input and encoding
    try:
        __StringCompressor.__require_valid_input_and_encoding("example", "utf-8")
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

def test_invalid_input_type():
    # Test with invalid input type (non-string)
    with pytest.raises(InvalidInputError):
        __StringCompressor.__require_valid_input_and_encoding(123, "utf-8")

def test_empty_input_string():
    # Test with empty input string
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.__require_valid_input_and_encoding("", "utf-8")
    assert str(excinfo.value) == 'Input string cannot be empty'

def test_invalid_encoding():
    # Test with invalid encoding type (non-string)
    with pytest.raises(ValueError):
        __StringCompressor.__require_valid_input_and_encoding("example", 123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding_happy_path
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding_happy_path.py:4:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""