
import pytest
import base64
import zlib
from string_utils.manipulation import __StringCompressor

def test_error_case_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        # Test invalid input type (should raise ValueError for invalid encoding)
        __StringCompressor.decompress("example", "invalid_encoding")
    assert str(excinfo.value) == "Invalid encoding provided: 'invalid_encoding'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_error_case_invalid_input.py F [100%]

=================================== FAILURES ===================================
________________________ test_error_case_invalid_input _________________________

    def test_error_case_invalid_input():
        with pytest.raises(ValueError) as excinfo:
            # Test invalid input type (should raise ValueError for invalid encoding)
            __StringCompressor.decompress("example", "invalid_encoding")
>       assert str(excinfo.value) == "Invalid encoding provided: 'invalid_encoding'"
E       assert 'Incorrect padding' == "Invalid enco...lid_encoding'"
E         
E         - Invalid encoding provided: 'invalid_encoding'
E         + Incorrect padding

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_error_case_invalid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_error_case_invalid_input.py::test_error_case_invalid_input
============================== 1 failed in 0.03s ===============================
"""