
import pytest
from isort._vendored.tomli._parser import parse_key_part

# Test cases for parse_key_part function

def test_parse_key_part_valid_bare_key():
    src = "example {'key': 'value'}"
    pos = 0
    new_pos, key_part = parse_key_part(src, pos)
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0.py F [100%]

=================================== FAILURES ===================================
______________________ test_parse_key_part_valid_bare_key ______________________

    def test_parse_key_part_valid_bare_key():
        src = "example {'key': 'value'}"
        pos = 0
        new_pos, key_part = parse_key_part(src, pos)
>       assert new_pos == len("example ") + 1
E       AssertionError: assert 7 == (8 + 1)
E        +  where 8 = len('example ')

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0.py::test_parse_key_part_valid_bare_key
============================== 1 failed in 0.09s ===============================
"""