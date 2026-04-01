
from isort._vendored.tomli._parser import parse_multiline_str, Pos
import pytest

def test_valid_basic_multiline_str():
    src = '"""This is a test string"""'
    pos = Pos(0)
    literal = False

    result = parse_multiline_str(src, pos, literal=literal)

    assert result == (len(src), '"This is a test string"')

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_valid_basic_multiline_str.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_basic_multiline_str ________________________

    def test_valid_basic_multiline_str():
        src = '"""This is a test string"""'
        pos = Pos(0)
        literal = False
    
        result = parse_multiline_str(src, pos, literal=literal)
    
>       assert result == (len(src), '"This is a test string"')
E       assert (27, 'This is a test string') == (27, '"This i...test string"')
E         
E         At index 1 diff: 'This is a test string' != '"This is a test string"'
E         Use -v to get more diff

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_valid_basic_multiline_str.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_multiline_str_3_test_valid_basic_multiline_str.py::test_valid_basic_multiline_str
============================== 1 failed in 0.13s ===============================
"""