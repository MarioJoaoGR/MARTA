
from string_utils.manipulation import __StringCompressor
import pytest

def is_string(value):
    return isinstance(value, str)

@pytest.mark.parametrize("input_string, encoding", [
    ("example", "utf-8"),
    ("another_example", "ascii")
])
def test_valid_input_and_encoding(input_string, encoding):
    try:
        __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
    except Exception as e:
        pytest.fail(f"Unexpected error occurred: {e}")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_________________ test_valid_input_and_encoding[example-utf-8] _________________

input_string = 'example', encoding = 'utf-8'

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),
        ("another_example", "ascii")
    ])
    def test_valid_input_and_encoding(input_string, encoding):
        try:
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:14: AttributeError

During handling of the above exception, another exception occurred:

input_string = 'example', encoding = 'utf-8'

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),
        ("another_example", "ascii")
    ])
    def test_valid_input_and_encoding(input_string, encoding):
        try:
            __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
        except Exception as e:
>           pytest.fail(f"Unexpected error occurred: {e}")
E           Failed: Unexpected error occurred: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:16: Failed
_____________ test_valid_input_and_encoding[another_example-ascii] _____________

input_string = 'another_example', encoding = 'ascii'

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),
        ("another_example", "ascii")
    ])
    def test_valid_input_and_encoding(input_string, encoding):
        try:
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:14: AttributeError

During handling of the above exception, another exception occurred:

input_string = 'another_example', encoding = 'ascii'

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),
        ("another_example", "ascii")
    ])
    def test_valid_input_and_encoding(input_string, encoding):
        try:
            __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
        except Exception as e:
>           pytest.fail(f"Unexpected error occurred: {e}")
E           Failed: Unexpected error occurred: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py::test_valid_input_and_encoding[example-utf-8]
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_valid_input_and_encoding.py::test_valid_input_and_encoding[another_example-ascii]
============================== 2 failed in 0.02s ===============================
"""