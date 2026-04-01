
import pytest
from flutes.multiproc import PoolType
from typing import Callable, List, Iterable, Any, Optional, Mapping
import multiprocessing as mp

@pytest.fixture
def pool():
    return PoolType()

def multiply(a, b):
    return a * b

def test_valid_case(pool: PoolType):
    args_list = [(1, 2), (3, 4), (5, 6)]
    result = pool.starmap_async(multiply, args_list)
    assert isinstance(result, mp.pool.ApplyResult)
    results = result.get()
    assert results == [2, 12, 30]

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

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

pool = <flutes.multiproc.PoolType state=RUN pool_size=128>

    def test_valid_case(pool: PoolType):
        args_list = [(1, 2), (3, 4), (5, 6)]
        result = pool.starmap_async(multiply, args_list)
>       assert isinstance(result, mp.pool.ApplyResult)
E       AssertionError: assert False
E        +  where False = isinstance(None, <class 'multiprocessing.pool.ApplyResult'>)
E        +    where <class 'multiprocessing.pool.ApplyResult'> = <module 'multiprocessing.pool' from '/usr/local/lib/python3.11/multiprocessing/pool.py'>.ApplyResult
E        +      where <module 'multiprocessing.pool' from '/usr/local/lib/python3.11/multiprocessing/pool.py'> = mp.pool

flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0_test_valid_case.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_PoolType_starmap_async_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.18s ===============================
"""