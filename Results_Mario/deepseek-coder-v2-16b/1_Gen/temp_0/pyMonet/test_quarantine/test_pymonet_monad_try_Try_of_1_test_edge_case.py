
import pytest
from pymonet.monad_try import Try

def test_edge_case():
    # Test None input
    result = Try.of(lambda: None)
    assert not result.is_success

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

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_of_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        # Test None input
        result = Try.of(lambda: None)
>       assert not result.is_success
E       assert not True
E        +  where True = <pymonet.monad_try.Try object at 0x7f8b963ec450>.is_success

pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_of_1_test_edge_case.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_monad_try_Try_of_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.06s ===============================
"""