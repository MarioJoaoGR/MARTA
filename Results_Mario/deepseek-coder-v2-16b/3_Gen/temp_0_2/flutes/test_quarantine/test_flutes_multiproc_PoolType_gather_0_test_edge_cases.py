
import pytest
from flutes.multiproc import PoolType
from typing import Callable, Iterator, Iterable, Any, Mapping

@pytest.fixture
def pool():
    return PoolType()

def test_gather(pool):
    def generate_numbers(n):
        for i in range(n):
            yield i * 2
    
    iterable = range(10)
    result_iter = pool.gather(generate_numbers, iterable, chunksize=2)
    assert list(result_iter) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_________________________________ test_gather __________________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_gather(pool):
        def generate_numbers(n):
            for i in range(n):
                yield i * 2
    
        iterable = range(10)
        result_iter = pool.gather(generate_numbers, iterable, chunksize=2)
>       assert list(result_iter) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
E       TypeError: 'NoneType' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_edge_cases.py:17: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_gather_0_test_edge_cases.py::test_gather
============================== 1 failed in 0.20s ===============================
"""