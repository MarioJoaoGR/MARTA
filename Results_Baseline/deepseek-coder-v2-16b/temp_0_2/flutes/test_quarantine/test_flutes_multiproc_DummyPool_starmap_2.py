
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

# Test Case 3: Testing starmap with a simple function and iterable
def test_dummy_pool_starmap():
    pool = DummyPool(processes=4)
    results = pool.starmap(lambda x, y: x + y, [(1, 2), (3, 4)])
    assert results == [3, 7]

# Test Case 4: Testing starmap with a function that takes multiple arguments and additional args/kwds
def test_dummy_pool_starmap_with_args_and_kwds():
    pool = DummyPool(processes=4)
    results = pool.starmap(lambda x, y, z: x + y + z, [(1, 2, 3), (4, 5, 6)], args=(0,), kwds={'z': 10})
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_2.py .F     [100%]

=================================== FAILURES ===================================
__________________ test_dummy_pool_starmap_with_args_and_kwds __________________

    def test_dummy_pool_starmap_with_args_and_kwds():
        pool = DummyPool(processes=4)
>       results = pool.starmap(lambda x, y, z: x + y + z, [(1, 2, 3), (4, 5, 6)], args=(0,), kwds={'z': 10})

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_2.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:95: in starmap
    return [fn(*x, *args, **kwds) for x in iterable]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f457c1c6590>

>   return [fn(*x, *args, **kwds) for x in iterable]
E   TypeError: test_dummy_pool_starmap_with_args_and_kwds.<locals>.<lambda>() got multiple values for argument 'z'

flutes/flutes/multiproc.py:95: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_2.py::test_dummy_pool_starmap_with_args_and_kwds
========================= 1 failed, 1 passed in 0.11s ==========================
"""