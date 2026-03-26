
import pytest
from isort._vendored.tomli._parser import parse_literal_str

# Test Case 1: Parsing a Simple Literal String
def test_parse_literal_str_simple():
    src = "hello 'world'"
    pos = 0
    new_pos, parsed_str = parse_literal_str(src, pos)
    assert parsed_str == "'hello 'world''"
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

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0.py F [100%]

=================================== FAILURES ===================================
________________________ test_parse_literal_str_simple _________________________

    def test_parse_literal_str_simple():
        src = "hello 'world'"
        pos = 0
        new_pos, parsed_str = parse_literal_str(src, pos)
>       assert parsed_str == "'hello 'world''"
E       assert 'ello ' == "'hello 'world''"
E         
E         - 'hello 'world''
E         + ello

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_literal_str_0.py::test_parse_literal_str_simple
============================== 1 failed in 0.10s ===============================
"""