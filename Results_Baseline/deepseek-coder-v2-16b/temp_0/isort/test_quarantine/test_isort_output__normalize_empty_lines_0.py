
import pytest
from isort.output import _normalize_empty_lines

# Test case 1: Normalize empty lines in a list with two empty strings
def test_normalize_empty_lines_two_empties():
    input_lines = ["", ""]
    expected_output = ['', '', '']
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_output__normalize_empty_lines_0.py F.     [100%]

=================================== FAILURES ===================================
____________________ test_normalize_empty_lines_two_empties ____________________

    def test_normalize_empty_lines_two_empties():
        input_lines = ["", ""]
        expected_output = ['', '', '']
>       assert _normalize_empty_lines(input_lines) == expected_output
E       AssertionError: assert [''] == ['', '', '']
E         
E         Right contains 2 more items, first extra item: ''
E         Use -v to get more diff

isort/Test4DT_tests/test_isort_output__normalize_empty_lines_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_output__normalize_empty_lines_0.py::test_normalize_empty_lines_two_empties
========================= 1 failed, 1 passed in 0.10s ==========================
"""