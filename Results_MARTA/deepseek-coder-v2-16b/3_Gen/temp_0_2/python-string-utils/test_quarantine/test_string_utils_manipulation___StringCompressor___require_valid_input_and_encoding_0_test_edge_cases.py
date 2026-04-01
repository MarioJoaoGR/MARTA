
import pytest
from string_utils.manipulation import __StringCompressor, InvalidInputError

def is_string(value):
    return isinstance(value, str)

@pytest.mark.parametrize("input_string, encoding", [
    ("example", "utf-8"),  # Valid call
    (123, "utf-8"),        # Raises InvalidInputError
    ("", "utf-8"),         # Raises ValueError
    ("example", 123)       # Raises ValueError
])
def test_edge_cases(input_string, encoding):
    with pytest.raises(InvalidInputError) as exc_info:
        __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_edge_cases[example-utf-8] ________________________

input_string = 'example', encoding = 'utf-8'

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),  # Valid call
        (123, "utf-8"),        # Raises InvalidInputError
        ("", "utf-8"),         # Raises ValueError
        ("example", 123)       # Raises ValueError
    ])
    def test_edge_cases(input_string, encoding):
        with pytest.raises(InvalidInputError) as exc_info:
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py:16: AttributeError
__________________________ test_edge_cases[123-utf-8] __________________________

input_string = 123, encoding = 'utf-8'

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),  # Valid call
        (123, "utf-8"),        # Raises InvalidInputError
        ("", "utf-8"),         # Raises ValueError
        ("example", 123)       # Raises ValueError
    ])
    def test_edge_cases(input_string, encoding):
        with pytest.raises(InvalidInputError) as exc_info:
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py:16: AttributeError
___________________________ test_edge_cases[-utf-8] ____________________________

input_string = '', encoding = 'utf-8'

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),  # Valid call
        (123, "utf-8"),        # Raises InvalidInputError
        ("", "utf-8"),         # Raises ValueError
        ("example", 123)       # Raises ValueError
    ])
    def test_edge_cases(input_string, encoding):
        with pytest.raises(InvalidInputError) as exc_info:
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py:16: AttributeError
_________________________ test_edge_cases[example-123] _________________________

input_string = 'example', encoding = 123

    @pytest.mark.parametrize("input_string, encoding", [
        ("example", "utf-8"),  # Valid call
        (123, "utf-8"),        # Raises InvalidInputError
        ("", "utf-8"),         # Raises ValueError
        ("example", 123)       # Raises ValueError
    ])
    def test_edge_cases(input_string, encoding):
        with pytest.raises(InvalidInputError) as exc_info:
>           __StringCompressor.__require_valid_input_and_encoding(input_string, encoding)
E           AttributeError: type object '__StringCompressor' has no attribute '__require_valid_input_and_encoding'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py:16: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py::test_edge_cases[example-utf-8]
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py::test_edge_cases[123-utf-8]
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py::test_edge_cases[-utf-8]
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringCompressor___require_valid_input_and_encoding_0_test_edge_cases.py::test_edge_cases[example-123]
============================== 4 failed in 0.03s ===============================
"""