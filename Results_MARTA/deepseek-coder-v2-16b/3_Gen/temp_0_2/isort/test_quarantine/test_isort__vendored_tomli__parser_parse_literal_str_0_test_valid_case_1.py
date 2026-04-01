
from isort._vendored.tomli._parser import parse_literal_str
import pytest

def test_valid_case_1():
    src = "''hello world'"
    pos = 0
    new_pos, lit_str = parse_literal_str(src, pos)
    assert new_pos == len("'hello world'")
    assert lit_str == "'hello world'"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0_test_valid_case_1.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        src = "''hello world'"
        pos = 0
        new_pos, lit_str = parse_literal_str(src, pos)
>       assert new_pos == len("'hello world'")
E       assert 2 == 13
E        +  where 13 = len("'hello world'")

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0_test_valid_case_1.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0_test_valid_case_1.py::test_valid_case_1
============================== 1 failed in 0.10s ===============================
"""