
import pytest
from string_utils.manipulation import __StringCompressor
from string_utils.errors import InvalidInputError

def test_valid_input_happy_path():
    with pytest.raises(InvalidInputError):
        __StringCompressor.__require_valid_input_and_encoding("", "utf-8")

    with pytest.raises(ValueError):
        __StringCompressor.__require_valid_input_and_encoding("example", 123)

    # Valid call should not raise any error
    __StringCompressor.__require_valid_input_and_encoding("example", "utf-8")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        with pytest.raises(InvalidInputError):
>           __StringCompressor.__require_valid_input_and_encoding("", "utf-8")
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_happy_path.py:8: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.04s ===============================
"""