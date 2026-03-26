
import pytest
from string_utils.manipulation import __StringCompressor
import base64
import zlib

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.decompress("")
    assert "Input should be a non-empty string representing a compressed data." in str(excinfo.value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError) as excinfo:
            __StringCompressor.decompress("")
>       assert "Input should be a non-empty string representing a compressed data." in str(excinfo.value)
E       AssertionError: assert 'Input should be a non-empty string representing a compressed data.' in 'Input string cannot be empty'
E        +  where 'Input string cannot be empty' = str(ValueError('Input string cannot be empty'))
E        +    where ValueError('Input string cannot be empty') = <ExceptionInfo ValueError('Input string cannot be empty') tblen=3>.value

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_invalid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""