
import pytest
from isort.core import _has_changed

def remove_whitespace(text, line_separator):
    return "".join(text.split())

@pytest.mark.parametrize("before, after, expected", [
    ("Hello, World!", "Hello, World!", False),
    (" Hello, World! ", "Hello, World!", True),
    ("Hello, World!", "Hello, World!\n", True),
    ("Hello, World!", "Hello, World!", True, {"line_separator": "."}),
    ("Hello, World!", "Hello, World!", False, {"ignore_whitespace": True})
])
def test_valid_case_line_separator_change(_has_changed, before, after, expected):
    assert _has_changed(before, after) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests/test_isort_core__has_changed_0_test_valid_case_line_separator_change.py _
Test4DT_tests/test_isort_core__has_changed_0_test_valid_case_line_separator_change.py::test_valid_case_line_separator_change: in "parametrize" the number of names (3):
  ['before', 'after', 'expected']
must be equal to the number of values (4):
  ('Hello, World!', 'Hello, World!', True, {'line_separator': '.'})
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort_core__has_changed_0_test_valid_case_line_separator_change.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.18s ===============================
"""