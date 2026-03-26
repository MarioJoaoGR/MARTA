
import pytest
from string_utils.manipulation import __StringCompressor

def is_string(value):
    return isinstance(value, str)

class InvalidInputError(Exception):
    pass

def test_invalid_inputs():
    with pytest.raises(InvalidInputError):
        __StringCompressor.__require_valid_input_and_encoding(123, "utf-8")
    
    with pytest.raises(ValueError):
        __StringCompressor.__require_valid_input_and_encoding("", "utf-8")
    
    with pytest.raises(ValueError):
        __StringCompressor.__require_valid_input_and_encoding("example", 123)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(InvalidInputError):
>           __StringCompressor.__require_valid_input_and_encoding(123, "utf-8")
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_invalid_inputs.py:13: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.03s ===============================
"""