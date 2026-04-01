
import pytest
from custom_exceptions import InvalidInputError
from string_utils.manipulation import __StringCompressor

def test_invalid_encoding():
    with pytest.raises(InvalidInputError):
        __StringCompressor.__require_valid_input_and_encoding("", "utf-8")

    with pytest.raises(ValueError):
        __StringCompressor.__require_valid_input_and_encoding("example", "")

    with pytest.raises(InvalidInputError):
        __StringCompressor.__require_valid_input_and_encoding(123, "utf-8")

    with pytest.raises(ValueError):
        __StringCompressor.__require_valid_input_and_encoding("example", None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_invalid_encoding
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_invalid_encoding.py:3:0: E0401: Unable to import 'custom_exceptions' (import-error)


"""