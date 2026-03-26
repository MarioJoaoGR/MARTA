
import pytest
from isort._vendored.tomli._parser import parse_basic_str, Pos

ILLEGAL_MULTILINE_BASIC_STR_CHARS = {'"', '\n', '\\'}
ILLEGAL_BASIC_STR_CHARS = {'\\', '\n'}

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        parse_basic_str('hello world', Pos(0), multiline=False)
    assert str(excinfo.value) == "Unterminated string"

    with pytest.raises(ValueError) as excinfo:
        parse_basic_str('"""this is a test', Pos(0), multiline=True)
    assert str(excinfo.value) == "Unterminated string"

    with pytest.raises(ValueError) as excinfo:
        parse_basic_str('hello world\\', Pos(0), multiline=False)
    assert str(excinfo.value) == 'Illegal character "\\"'

    with pytest.raises(ValueError) as excinfo:
        parse_basic_str('"""this is a test\\', Pos(0), multiline=True)
    assert str(excinfo.value) == 'Illegal character "\\"'

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError) as excinfo:
            parse_basic_str('hello world', Pos(0), multiline=False)
>       assert str(excinfo.value) == "Unterminated string"
E       AssertionError: assert 'Unterminated... of document)' == 'Unterminated string'
E         
E         - Unterminated string
E         + Unterminated string (at end of document)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_input.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.12s ===============================
"""