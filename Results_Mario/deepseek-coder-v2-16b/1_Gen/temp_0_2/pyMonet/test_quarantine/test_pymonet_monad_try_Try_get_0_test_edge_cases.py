
import pytest
from pymonet.monad_try import Try

def test_get():
    # Test when the operation is successful
    success_try = Try(10, is_success=True)
    assert success_try.get() == 10

    # Test when the operation fails
    failure_try = Try("error", is_success=False)
    with pytest.raises(RuntimeError):
        failure_try.get()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_get_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________________ test_get ___________________________________

    def test_get():
        # Test when the operation is successful
        success_try = Try(10, is_success=True)
        assert success_try.get() == 10
    
        # Test when the operation fails
        failure_try = Try("error", is_success=False)
>       with pytest.raises(RuntimeError):
E       Failed: DID NOT RAISE <class 'RuntimeError'>

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_get_0_test_edge_cases.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_get_0_test_edge_cases.py::test_get
============================== 1 failed in 0.06s ===============================
"""