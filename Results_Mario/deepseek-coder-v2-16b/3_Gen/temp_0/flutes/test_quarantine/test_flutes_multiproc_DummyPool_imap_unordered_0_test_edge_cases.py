
import pytest
from flutes.multiproc import DummyPool

def test_edge_cases():
    # Test when processes is zero
    pool = DummyPool(processes=0)
    assert pool._state == 1, f"Expected _state to be 1 but got {pool._state}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test when processes is zero
        pool = DummyPool(processes=0)
>       assert pool._state == 1, f"Expected _state to be 1 but got {pool._state}"
E       AssertionError: Expected _state to be 1 but got RUN
E       assert 'RUN' == 1
E        +  where 'RUN' = <flutes.multiproc.DummyPool object at 0x7f988d5a4090>._state

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_0_test_edge_cases.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_imap_unordered_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.11s ===============================
"""