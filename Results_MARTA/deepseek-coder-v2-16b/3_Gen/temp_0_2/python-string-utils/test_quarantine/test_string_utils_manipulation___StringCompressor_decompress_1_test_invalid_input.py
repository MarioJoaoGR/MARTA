
import pytest
from string_utils.manipulation import __StringCompressor

class Test__StringCompressor:
    def test_invalid_input(self):
        # Test when input is not a string
        with pytest.raises(ValueError) as context:
            __StringCompressor.decompress(12345)
        assert str(context.value) == "Invalid input: expected a string, but got <class 'int'>"

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
__________________ Test__StringCompressor.test_invalid_input ___________________

self = <Test4DT_tests.test_string_utils_manipulation___StringCompressor_decompress_1_test_invalid_input.Test__StringCompressor object at 0x1063e72e0>

    def test_invalid_input(self):
        # Test when input is not a string
        with pytest.raises(ValueError) as context:
>           __StringCompressor.decompress(12345)
E           NameError: name '_Test__StringCompressor__StringCompressor' is not defined

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_invalid_input.py:9: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor_decompress_1_test_invalid_input.py::Test__StringCompressor::test_invalid_input
============================== 1 failed in 0.03s ===============================
"""