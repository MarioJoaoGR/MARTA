
import pytest
from isort._vendored.tomli._parser import parse_basic_str, Pos

def test_valid_multi_line():
    src = '"""This is a multi-line string."""'
    pos = Pos(0)
    multiline = True
    
    result = parse_basic_str(src, pos, multiline=multiline)
    
    assert isinstance(result, tuple), "Result should be a tuple"
    assert len(result) == 2, "Result tuple should have two elements"
    assert isinstance(result[0], Pos), "First element of the result should be an instance of Pos"
    assert isinstance(result[1], str), "Second element of the result should be a string"
    assert result[0] == 3 + pos, f"Expected position to be {3 + pos}, but got {result[0]}"
    assert result[1] == src[:-3], f"Expected parsed string to be '{src[:-3]}', but got '{result[1]}'"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_valid_multi_line.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_multi_line _____________________________

    def test_valid_multi_line():
        src = '"""This is a multi-line string."""'
        pos = Pos(0)
        multiline = True
    
        result = parse_basic_str(src, pos, multiline=multiline)
    
        assert isinstance(result, tuple), "Result should be a tuple"
        assert len(result) == 2, "Result tuple should have two elements"
        assert isinstance(result[0], Pos), "First element of the result should be an instance of Pos"
        assert isinstance(result[1], str), "Second element of the result should be a string"
        assert result[0] == 3 + pos, f"Expected position to be {3 + pos}, but got {result[0]}"
>       assert result[1] == src[:-3], f"Expected parsed string to be '{src[:-3]}', but got '{result[1]}'"
E       AssertionError: Expected parsed string to be '"""This is a multi-line string.', but got ''
E       assert '' == '"""This is a...-line string.'
E         
E         - """This is a multi-line string.

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_valid_multi_line.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_valid_multi_line.py::test_valid_multi_line
============================== 1 failed in 0.11s ===============================
"""