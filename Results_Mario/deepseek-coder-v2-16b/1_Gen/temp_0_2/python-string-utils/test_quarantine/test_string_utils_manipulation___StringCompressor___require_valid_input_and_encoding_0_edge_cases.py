
import pytest
from string_utils.manipulation import __StringCompressor

def is_string(value):
    return isinstance(value, str)

def test_require_valid_input_and_encoding_valid():
    try:
        __StringCompressor.__require_valid_input_and_encoding("example", "utf-8")
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

def test_require_valid_input_and_encoding_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.__require_valid_input_and_encoding(123, "utf-8")
    assert str(excinfo.value) == 'Expected "str", received "<class \'int\'>"'

def test_require_valid_input_and_encoding_empty_string():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.__require_valid_input_and_encoding("", "utf-8")
    assert str(excinfo.value) == 'Input string cannot be empty'

def test_require_valid_input_and_encoding_invalid_encoding():
    with pytest.raises(ValueError) as excinfo:
        __StringCompressor.__require_valid_input_and_encoding("example", 123)
    assert str(excinfo.value) == 'Invalid encoding'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_________________ test_require_valid_input_and_encoding_valid __________________

    def test_require_valid_input_and_encoding_valid():
        try:
>           __StringCompressor.__require_valid_input_and_encoding("example", "utf-8")
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py:10: AttributeError

During handling of the above exception, another exception occurred:

    def test_require_valid_input_and_encoding_valid():
        try:
            __StringCompressor.__require_valid_input_and_encoding("example", "utf-8")
        except Exception as e:
>           pytest.fail(f"Unexpected error occurred: {e}")
E           Failed: Unexpected error occurred: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py:12: Failed
_____________ test_require_valid_input_and_encoding_invalid_input ______________

    def test_require_valid_input_and_encoding_invalid_input():
        with pytest.raises(ValueError) as excinfo:
>           __StringCompressor.__require_valid_input_and_encoding(123, "utf-8")
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py:16: AttributeError
______________ test_require_valid_input_and_encoding_empty_string ______________

    def test_require_valid_input_and_encoding_empty_string():
        with pytest.raises(ValueError) as excinfo:
>           __StringCompressor.__require_valid_input_and_encoding("", "utf-8")
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py:21: AttributeError
____________ test_require_valid_input_and_encoding_invalid_encoding ____________

    def test_require_valid_input_and_encoding_invalid_encoding():
        with pytest.raises(ValueError) as excinfo:
>           __StringCompressor.__require_valid_input_and_encoding("example", 123)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py:26: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py::test_require_valid_input_and_encoding_valid
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py::test_require_valid_input_and_encoding_invalid_input
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py::test_require_valid_input_and_encoding_empty_string
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_edge_cases.py::test_require_valid_input_and_encoding_invalid_encoding
============================== 4 failed in 0.05s ===============================
"""