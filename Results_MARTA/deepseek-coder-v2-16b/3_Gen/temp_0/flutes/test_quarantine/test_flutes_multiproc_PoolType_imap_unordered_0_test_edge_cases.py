
import pytest
from flutes.multiproc import PoolType  # Assuming this is the correct module path

@pytest.fixture
def pool():
    return PoolType()

def test_edge_cases(pool):
    def square(x):
        return x ** 2
    
    iterable = range(5)
    result_iterator = pool.imap_unordered(square, iterable, chunksize=1)
    results = list(result_iterator)
    
    assert len(results) == 5
    for expected, actual in zip(range(5), results):
        assert expected ** 2 == actual

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_edge_cases(pool):
        def square(x):
            return x ** 2
    
        iterable = range(5)
        result_iterator = pool.imap_unordered(square, iterable, chunksize=1)
>       results = list(result_iterator)
E       TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_edge_cases.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_imap_unordered_0_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.20s ===============================
"""