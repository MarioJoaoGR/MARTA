
import pytest
from pytutils.excs import ok

def test_invalid_input_non_exception_type():
    with pytest.raises(TypeError):
        with ok():
            raise ValueError("This should not be caught by the context manager")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_excs_ok_3_test_invalid_input_non_exception_type.py F [100%]

=================================== FAILURES ===================================
____________________ test_invalid_input_non_exception_type _____________________

    def test_invalid_input_non_exception_type():
        with pytest.raises(TypeError):
            with ok():
>               raise ValueError("This should not be caught by the context manager")
E               ValueError: This should not be caught by the context manager

pytutils/Test4DT_tests/test_pytutils_excs_ok_3_test_invalid_input_non_exception_type.py:8: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_excs_ok_3_test_invalid_input_non_exception_type.py::test_invalid_input_non_exception_type
============================== 1 failed in 0.06s ===============================
"""