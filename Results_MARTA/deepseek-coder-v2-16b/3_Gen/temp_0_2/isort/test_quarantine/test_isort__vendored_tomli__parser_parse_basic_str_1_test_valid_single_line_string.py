
import pytest
from isort._vendored.tomli._parser import parse_basic_str

def test_valid_single_line_string():
    src = 'Hello "world"'
    pos = 0
    new_pos, parsed_str = parse_basic_str(src, pos, multiline=False)
    assert parsed_str == 'Hello "world"', f"Expected 'Hello \"world\"', but got {parsed_str}"

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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_1_test_valid_single_line_string.py F [100%]

=================================== FAILURES ===================================
________________________ test_valid_single_line_string _________________________

    def test_valid_single_line_string():
        src = 'Hello "world"'
        pos = 0
        new_pos, parsed_str = parse_basic_str(src, pos, multiline=False)
>       assert parsed_str == 'Hello "world"', f"Expected 'Hello \"world\"', but got {parsed_str}"
E       AssertionError: Expected 'Hello "world"', but got Hello 
E       assert 'Hello ' == 'Hello "world"'
E         
E         - Hello "world"
E         + Hello

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_1_test_valid_single_line_string.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_basic_str_1_test_valid_single_line_string.py::test_valid_single_line_string
============================== 1 failed in 0.12s ===============================
"""