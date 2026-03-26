
from isort._vendored.tomli._parser import Pos, parse_key_value_pair
import pytest

def test_valid_input_happy_path():
    src = 'name = 3.14'
    pos = Pos(0)
    parsed_pos, parsed_key, value = parse_key_value_pair(src, pos, float)
    
    assert parsed_pos == Pos(8)

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        src = 'name = 3.14'
        pos = Pos(0)
        parsed_pos, parsed_key, value = parse_key_value_pair(src, pos, float)
    
>       assert parsed_pos == Pos(8)
E       assert 11 == 8
E        +  where 8 = Pos(8)

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_valid_input_happy_path.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_key_value_pair_0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.10s ===============================
"""