
import multiprocessing
from flutes.multiproc import DummyPool, DummyApplyResult

def test_edge_case():
    pool = DummyPool(processes=0)
    results = list(pool.map_async(lambda x: x * 2, [1, 2, 3]))
    assert results == [2, 4, 6]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        pool = DummyPool(processes=0)
>       results = list(pool.map_async(lambda x: x * 2, [1, 2, 3]))
E       TypeError: 'DummyApplyResult' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_edge_case.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_map_async_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.10s ===============================
"""