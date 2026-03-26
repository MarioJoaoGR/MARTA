
import pytest
from flutes.multiproc import PoolType

def test_imap_unordered():
    pool = PoolType()
    
    def square(x):
        return x ** 2
    
    iterable = range(10)
    results = list(pool.imap_unordered(square, iterable))
    
    expected_results = [x**2 for x in range(10)]
    assert results == expected_results

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_imap_unordered ______________________________

    def test_imap_unordered():
        pool = PoolType()
    
        def square(x):
            return x ** 2
    
        iterable = range(10)
>       results = list(pool.imap_unordered(square, iterable))
E       TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_edge_cases.py:12: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_edge_cases.py::test_imap_unordered
============================== 1 failed in 0.19s ===============================
"""