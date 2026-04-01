
from custom_exceptions import InvalidInputError
import pytest
from string_utils.manipulation import __StringCompressor

def is_string(value):
    return isinstance(value, str)

@pytest.mark.parametrize("input_string, encoding", [
    (123, "utf-8"),  # Invalid input type
    ("example", None),  # Invalid encoding type
    ("example", "")  # Empty encoding string
])
def test_invalid_input_string(__StringCompressor, input_string, encoding):
    with pytest.raises(InvalidInputError) as excinfo:
        __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
    assert str(excinfo.value) == f'Expected "str", received "{type(input_string).__name__}"'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_invalid_input_string
python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_invalid_input_string.py:2:0: E0401: Unable to import 'custom_exceptions' (import-error)

"""