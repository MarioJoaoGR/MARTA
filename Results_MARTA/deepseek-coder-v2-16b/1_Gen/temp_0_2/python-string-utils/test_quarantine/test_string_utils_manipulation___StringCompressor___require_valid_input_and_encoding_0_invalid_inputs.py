
import pytest
from string_utils.manipulation import is_string, InvalidInputError

class __StringCompressor:
    @staticmethod
    def __require_valid_input_and_encoding(input_string: str, encoding: str):
        """
        Validates the input string and encoding to ensure they are valid for compression operations.
        
        This method checks if the provided `input_string` is a non-empty string and if the `encoding` is also a string. If any of these conditions are not met, it raises an appropriate error.
        
        Parameters:
            input_string (str): The string that needs to be validated for compression.
            encoding (str): The encoding type used for compressing the string. Must be a non-empty string representing a valid encoding format.
            
        Raises:
            InvalidInputError: If `input_string` is not a string or is an empty string, this error will be raised with a message indicating that the input should be a string and cannot be empty.
            ValueError: If `encoding` is not a string or is an empty string, this error will be raised with a message indicating that the encoding must be a valid string.
            
        Example:
            >>> __StringCompressor.__require_valid_input_and_encoding("example", "utf-8")  # This would pass validation as both parameters are valid strings.
            >>> try:
            ...     __StringCompressor.__require_valid_input_and_encoding(123, "utf-8")
            ... except ValueError as e:
            ...     print(e)  # Output: Expected "str", received "<class 'int'>"
            
            In this example, attempting to pass an integer instead of a string for `input_string` would raise a ValueError.
        """
        if not is_string(input_string):
            raise InvalidInputError(f'Expected {type(str)} but got {type(input_string)}')

        if len(input_string) == 0:
            raise ValueError('Input string cannot be empty')

        if not is_string(encoding):
            raise ValueError('Invalid encoding')

@pytest.mark.parametrize("input_string, encoding", [
    (123, "utf-8"),  # input_string is not a string
    ("example", None),  # encoding is None
    ("example", 123)  # encoding is not a string
])
def test_require_valid_input_and_encoding_invalid_inputs(input_string, encoding):
    with pytest.raises(ValueError):
        __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_invalid_inputs.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______ test_require_valid_input_and_encoding_invalid_inputs[123-utf-8] ________

input_string = 123, encoding = 'utf-8'

    @pytest.mark.parametrize("input_string, encoding", [
        (123, "utf-8"),  # input_string is not a string
        ("example", None),  # encoding is None
        ("example", 123)  # encoding is not a string
    ])
    def test_require_valid_input_and_encoding_invalid_inputs(input_string, encoding):
        with pytest.raises(ValueError):
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_invalid_inputs.py:46: AttributeError
______ test_require_valid_input_and_encoding_invalid_inputs[example-None] ______

input_string = 'example', encoding = None

    @pytest.mark.parametrize("input_string, encoding", [
        (123, "utf-8"),  # input_string is not a string
        ("example", None),  # encoding is None
        ("example", 123)  # encoding is not a string
    ])
    def test_require_valid_input_and_encoding_invalid_inputs(input_string, encoding):
        with pytest.raises(ValueError):
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_invalid_inputs.py:46: AttributeError
______ test_require_valid_input_and_encoding_invalid_inputs[example-123] _______

input_string = 'example', encoding = 123

    @pytest.mark.parametrize("input_string, encoding", [
        (123, "utf-8"),  # input_string is not a string
        ("example", None),  # encoding is None
        ("example", 123)  # encoding is not a string
    ])
    def test_require_valid_input_and_encoding_invalid_inputs(input_string, encoding):
        with pytest.raises(ValueError):
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_invalid_inputs.py:46: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_invalid_inputs.py::test_require_valid_input_and_encoding_invalid_inputs[123-utf-8]
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_invalid_inputs.py::test_require_valid_input_and_encoding_invalid_inputs[example-None]
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_invalid_inputs.py::test_require_valid_input_and_encoding_invalid_inputs[example-123]
============================== 3 failed in 0.04s ===============================
"""