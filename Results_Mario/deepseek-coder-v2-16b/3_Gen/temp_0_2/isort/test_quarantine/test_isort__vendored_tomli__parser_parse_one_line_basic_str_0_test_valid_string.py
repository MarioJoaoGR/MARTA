
from isort._vendored.tomli._parser import parse_one_line_basic_str
from typing import Tuple

def test_valid_string():
    src = 'Hello "world"'
    pos = 0
    new_pos, parsed_str = parse_one_line_basic_str(src, pos)
    assert parsed_str == '"world"', f"Expected 'world' but got {parsed_str}"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_valid_string.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_string _______________________________

    def test_valid_string():
        src = 'Hello "world"'
        pos = 0
        new_pos, parsed_str = parse_one_line_basic_str(src, pos)
>       assert parsed_str == '"world"', f"Expected 'world' but got {parsed_str}"
E       AssertionError: Expected 'world' but got ello 
E       assert 'ello ' == '"world"'
E         
E         - "world"
E         + ello

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_valid_string.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_one_line_basic_str_0_test_valid_string.py::test_valid_string
============================== 1 failed in 0.10s ===============================
"""