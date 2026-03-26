
from isort.output import _output_as_string, _normalize_empty_lines
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("lines, separator, expected", [
    (["line1", "line2"], "\n", "line1\nline2\n"),
    (["line1", "", "", "line2"], " ", "line1  line2 "),
    (["last line"], "-", "last line-")
])
@patch('isort.output._normalize_empty_lines')
def test_invalid_separator(mock_normalize, lines, separator, expected):
    mock_normalize.return_value = lines
    result = _output_as_string(lines, separator)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_output__output_as_string_1_test_invalid_separator.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________ test_invalid_separator[lines0-\n-line1\nline2\n] _______________

mock_normalize = <MagicMock name='_normalize_empty_lines' id='140318753678032'>
lines = ['line1', 'line2'], separator = '\n', expected = 'line1\nline2\n'

    @pytest.mark.parametrize("lines, separator, expected", [
        (["line1", "line2"], "\n", "line1\nline2\n"),
        (["line1", "", "", "line2"], " ", "line1  line2 "),
        (["last line"], "-", "last line-")
    ])
    @patch('isort.output._normalize_empty_lines')
    def test_invalid_separator(mock_normalize, lines, separator, expected):
        mock_normalize.return_value = lines
        result = _output_as_string(lines, separator)
>       assert result == expected
E       AssertionError: assert 'line1\nline2' == 'line1\nline2\n'
E         
E           line1
E         - line2
E         ?      -
E         + line2

isort/Test4DT_tests/test_isort_output__output_as_string_1_test_invalid_separator.py:15: AssertionError
________________ test_invalid_separator[lines1- -line1  line2 ] ________________

mock_normalize = <MagicMock name='_normalize_empty_lines' id='140318751389264'>
lines = ['line1', '', '', 'line2'], separator = ' ', expected = 'line1  line2 '

    @pytest.mark.parametrize("lines, separator, expected", [
        (["line1", "line2"], "\n", "line1\nline2\n"),
        (["line1", "", "", "line2"], " ", "line1  line2 "),
        (["last line"], "-", "last line-")
    ])
    @patch('isort.output._normalize_empty_lines')
    def test_invalid_separator(mock_normalize, lines, separator, expected):
        mock_normalize.return_value = lines
        result = _output_as_string(lines, separator)
>       assert result == expected
E       AssertionError: assert 'line1   line2' == 'line1  line2 '
E         
E         - line1  line2 
E         ?             -
E         + line1   line2
E         ?        +

isort/Test4DT_tests/test_isort_output__output_as_string_1_test_invalid_separator.py:15: AssertionError
_________________ test_invalid_separator[lines2---last line-] __________________

mock_normalize = <MagicMock name='_normalize_empty_lines' id='140318751275536'>
lines = ['last line'], separator = '-', expected = 'last line-'

    @pytest.mark.parametrize("lines, separator, expected", [
        (["line1", "line2"], "\n", "line1\nline2\n"),
        (["line1", "", "", "line2"], " ", "line1  line2 "),
        (["last line"], "-", "last line-")
    ])
    @patch('isort.output._normalize_empty_lines')
    def test_invalid_separator(mock_normalize, lines, separator, expected):
        mock_normalize.return_value = lines
        result = _output_as_string(lines, separator)
>       assert result == expected
E       AssertionError: assert 'last line' == 'last line-'
E         
E         - last line-
E         ?          -
E         + last line

isort/Test4DT_tests/test_isort_output__output_as_string_1_test_invalid_separator.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_output__output_as_string_1_test_invalid_separator.py::test_invalid_separator[lines0-\n-line1\nline2\n]
FAILED isort/Test4DT_tests/test_isort_output__output_as_string_1_test_invalid_separator.py::test_invalid_separator[lines1- -line1  line2 ]
FAILED isort/Test4DT_tests/test_isort_output__output_as_string_1_test_invalid_separator.py::test_invalid_separator[lines2---last line-]
============================== 3 failed in 0.12s ===============================
"""