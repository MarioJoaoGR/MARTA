
import pytest
from isort._vendored.tomli._parser import parse_value, Pos

def test_valid_basic_string():
    src = '"hello world"'
    pos = Pos(0)
    parsed_str, _ = parse_value(src, pos, float)
    assert parsed_str == "hello world"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_0_test_valid_basic_string.py F [100%]

=================================== FAILURES ===================================
___________________________ test_valid_basic_string ____________________________

    def test_valid_basic_string():
        src = '"hello world"'
        pos = Pos(0)
        parsed_str, _ = parse_value(src, pos, float)
>       assert parsed_str == "hello world"
E       AssertionError: assert 13 == 'hello world'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_0_test_valid_basic_string.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_0_test_valid_basic_string.py::test_valid_basic_string
============================== 1 failed in 0.10s ===============================
"""