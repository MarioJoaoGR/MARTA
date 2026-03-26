
import pytest
from isort._vendored.tomli._parser import parse_basic_str, Pos

def test_valid_multi_line():
    src = '"""this is a test"""'
    pos = Pos(0)
    _, parsed_str = parse_basic_str(src, pos, multiline=True)
    assert parsed_str == "this is a test"

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
        src = '"""this is a test"""'
        pos = Pos(0)
        _, parsed_str = parse_basic_str(src, pos, multiline=True)
>       assert parsed_str == "this is a test"
E       AssertionError: assert '' == 'this is a test'
E         
E         - this is a test

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_valid_multi_line.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_0_test_valid_multi_line.py::test_valid_multi_line
============================== 1 failed in 0.11s ===============================
"""