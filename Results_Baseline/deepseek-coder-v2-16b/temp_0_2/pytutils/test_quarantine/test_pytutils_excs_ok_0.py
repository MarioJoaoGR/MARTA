
import pytest
from pytutils.excs import ok

# Test that the context manager handles specified exceptions gracefully
def test_ok_with_specified_exceptions():
    with pytest.raises(ZeroDivisionError):
        with ok(ZeroDivisionError):
            raise ZeroDivisionError("division by zero")

# Test that the context manager raises other exceptions
def test_ok_raises_other_exceptions():
    with pytest.raises(ValueError) as excinfo:
        with ok(ZeroDivisionError):
            raise ValueError("Test exception")
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

pytutils/Test4DT_tests/test_pytutils_excs_ok_0.py F.                     [100%]

=================================== FAILURES ===================================
______________________ test_ok_with_specified_exceptions _______________________

    def test_ok_with_specified_exceptions():
>       with pytest.raises(ZeroDivisionError):
E       Failed: DID NOT RAISE <class 'ZeroDivisionError'>

pytutils/Test4DT_tests/test_pytutils_excs_ok_0.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_excs_ok_0.py::test_ok_with_specified_exceptions
========================= 1 failed, 1 passed in 0.06s ==========================
"""