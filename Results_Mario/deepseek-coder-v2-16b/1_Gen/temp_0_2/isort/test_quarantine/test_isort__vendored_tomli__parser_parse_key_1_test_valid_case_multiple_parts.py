
from isort._vendored.tomli._parser import parse_key, Pos, Key
import pytest

def test_valid_case_multiple_parts():
    src = 'user.name'
    pos = Pos(0)
    
    result_pos, result_key = parse_key(src, pos)
    
    assert result_pos == 7

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_case_multiple_parts.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_case_multiple_parts ________________________

    def test_valid_case_multiple_parts():
        src = 'user.name'
        pos = Pos(0)
    
        result_pos, result_key = parse_key(src, pos)
    
>       assert result_pos == 7
E       assert 9 == 7

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_case_multiple_parts.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_1_test_valid_case_multiple_parts.py::test_valid_case_multiple_parts
============================== 1 failed in 0.10s ===============================
"""