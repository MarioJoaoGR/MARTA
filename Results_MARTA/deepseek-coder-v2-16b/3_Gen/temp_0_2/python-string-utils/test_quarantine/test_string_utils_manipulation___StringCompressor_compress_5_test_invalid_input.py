
import pytest
from string_utils.manipulation import __StringCompressor

def test_invalid_input():
    with pytest.raises(ValueError):
        # Test case for invalid input type (should raise ValueError)
        __StringCompressor.compress(123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_compress_5_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError):
            # Test case for invalid input type (should raise ValueError)
>           __StringCompressor.compress(123)

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_compress_5_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
python-string-utils/string_utils/manipulation.py:174: in compress
    cls.__require_valid_input_and_encoding(input_string, encoding)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = 123, encoding = 'utf-8'

    @staticmethod
    def __require_valid_input_and_encoding(input_string: str, encoding: str):
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "int"

python-string-utils/string_utils/manipulation.py:164: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_compress_5_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""