
import pytest
from isort._vendored.tomli._parser import parse_key_part, BARE_KEY_CHARS, skip_chars

def test_valid_key_part_happy_path():
    src = "example {'key': 'value'}"
    pos = 0
    new_pos, key_part = parse_key_part(src, pos)
    
    assert new_pos == len("example ")  # The length of the string before the key part

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_valid_key_part_happy_path.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_key_part_happy_path ________________________

    def test_valid_key_part_happy_path():
        src = "example {'key': 'value'}"
        pos = 0
        new_pos, key_part = parse_key_part(src, pos)
    
>       assert new_pos == len("example ")  # The length of the string before the key part
E       AssertionError: assert 7 == 8
E        +  where 8 = len('example ')

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_valid_key_part_happy_path.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_valid_key_part_happy_path.py::test_valid_key_part_happy_path
============================== 1 failed in 0.10s ===============================
"""