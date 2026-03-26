
import pytest
from pytutils.excs import ok

class TestOk:
    def test_ok(self):
        with pytest.raises(AssertionError):
            with ok():
                # This should not raise any error
                assert len([]) == 0, "This should not raise any error"

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

pytutils/Test4DT_tests/test_pytutils_excs_ok_4_test_edge_case_empty_list.py F [100%]

=================================== FAILURES ===================================
________________________________ TestOk.test_ok ________________________________

self = <Test4DT_tests.test_pytutils_excs_ok_4_test_edge_case_empty_list.TestOk object at 0x7f26c1f3a750>

    def test_ok(self):
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

pytutils/Test4DT_tests/test_pytutils_excs_ok_4_test_edge_case_empty_list.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_excs_ok_4_test_edge_case_empty_list.py::TestOk::test_ok
============================== 1 failed in 0.05s ===============================
"""