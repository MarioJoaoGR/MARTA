
from isort._vendored.tomli._parser import parse_one_line_basic_str, Pos
import pytest

def test_valid_single_line_string():
    src = '"Hello, World!"'
    pos = Pos(0)

    result = parse_one_line_basic_str(src, pos)

    assert isinstance(result[1], str), "The parsed result should be a string"
    assert result[1] == 'Hello, World!', f"Expected 'Hello, World!' but got {result[1]}"
    assert result[0].offset == len(src), "The position offset should be at the end of the string"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_valid_single_line_string.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_single_line_string _________________________

    def test_valid_single_line_string():
        src = '"Hello, World!"'
        pos = Pos(0)
    
        result = parse_one_line_basic_str(src, pos)
    
        assert isinstance(result[1], str), "The parsed result should be a string"
        assert result[1] == 'Hello, World!', f"Expected 'Hello, World!' but got {result[1]}"
>       assert result[0].offset == len(src), "The position offset should be at the end of the string"
E       AttributeError: 'int' object has no attribute 'offset'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_valid_single_line_string.py:13: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_valid_single_line_string.py::test_valid_single_line_string
============================== 1 failed in 0.10s ===============================
"""