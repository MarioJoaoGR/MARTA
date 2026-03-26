
import pytest
from isort.literal import assignments, AssignmentsFormatMismatch

# Test Case 1: Basic functionality with multiple variable assignments
def test_assignments_basic():
    code = """var2 = 20
    var3 = 30
    var1 = 10"""
    result = assignments(code)
    assert result == "var1 = 10\nvar2 = 20\nvar3 = 30"

# Test Case 2: Basic functionality with different variable names and values
def test_assignments_different():
    code = """x = 1
    y = 2
    z = 3"""
    result = assignments(code)
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

isort/Test4DT_tests/test_isort_literal_assignments_0.py F.               [100%]

=================================== FAILURES ===================================
____________________________ test_assignments_basic ____________________________

    def test_assignments_basic():
        code = """var2 = 20
        var3 = 30
        var1 = 10"""
        result = assignments(code)
>       assert result == "var1 = 10\nvar2 = 20\nvar3 = 30"
E       AssertionError: assert '    var1 = 1...\nvar2 = 20\n' == 'var1 = 10\nv...20\nvar3 = 30'
E         
E         - var1 = 10
E         +     var1 = 10    var3 = 30
E           var2 = 20
E         - var3 = 30

isort/Test4DT_tests/test_isort_literal_assignments_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_literal_assignments_0.py::test_assignments_basic
========================= 1 failed, 1 passed in 0.10s ==========================
"""