
import pytest
from multiprocessing import Pool
from flutes.multiproc import DummyPool

def test_dummy_pool_without_initializer():
    pool = DummyPool(processes=0)
    results = list(pool.gather(lambda x: [x], range(5)))
    assert results == [[0], [1], [2], [3], [4]]

def test_dummy_pool_with_initializer():
    def initializer_func(arg):
        print(f"Initializing with arg: {arg}")
    
    pool = DummyPool(processes=0, initializer=initializer_func, initargs=(42,))
    results = list(pool.gather(lambda x: [x], range(5)))
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

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0.py F.      [100%]

=================================== FAILURES ===================================
_____________________ test_dummy_pool_without_initializer ______________________

    def test_dummy_pool_without_initializer():
        pool = DummyPool(processes=0)
        results = list(pool.gather(lambda x: [x], range(5)))
>       assert results == [[0], [1], [2], [3], [4]]
E       assert [0, 1, 2, 3, 4] == [[0], [1], [2], [3], [4]]
E         
E         At index 0 diff: 0 != [0]
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_gather_0.py::test_dummy_pool_without_initializer
========================= 1 failed, 1 passed in 0.10s ==========================
"""