
from isort._vendored.tomli._parser import parse_key_part, Pos
import pytest

def test_valid_key_parse():
    src = 'key123'
    pos = Pos(0)  # Initialize Pos object with the starting position
    new_pos, parsed_key = parse_key_part(src, pos)
    
    assert new_pos.value == len(parsed_key), f"Expected new_pos to be {len(parsed_key)}, but got {new_pos.value}"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_valid_key_parse.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_key_parse _____________________________

    def test_valid_key_parse():
        src = 'key123'
        pos = Pos(0)  # Initialize Pos object with the starting position
        new_pos, parsed_key = parse_key_part(src, pos)
    
>       assert new_pos.value == len(parsed_key), f"Expected new_pos to be {len(parsed_key)}, but got {new_pos.value}"
E       AttributeError: 'int' object has no attribute 'value'

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_valid_key_parse.py:10: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_part_0_test_valid_key_parse.py::test_valid_key_parse
============================== 1 failed in 0.10s ===============================
"""