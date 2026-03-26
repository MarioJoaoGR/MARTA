
import pytest
from multiprocessing import Pool
from typing import Callable, Iterable, List, Tuple, Any
from flutes.multiproc import DummyPool

# Test cases for the DummyPool class and its starmap method
def test_dummy_pool_starmap_with_args():
    def multiply(a, b):
        return a * b
    
    pool = DummyPool(processes=0)
    results = pool.starmap(multiply, [(1, 2), (3, 4)], args=(5,))
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

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_1.py F      [100%]

=================================== FAILURES ===================================
______________________ test_dummy_pool_starmap_with_args _______________________

    def test_dummy_pool_starmap_with_args():
        def multiply(a, b):
            return a * b
    
        pool = DummyPool(processes=0)
>       results = pool.starmap(multiply, [(1, 2), (3, 4)], args=(5,))

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_1.py:13: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/multiproc.py:95: in starmap
    return [fn(*x, *args, **kwds) for x in iterable]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f881fac08b0>

>   return [fn(*x, *args, **kwds) for x in iterable]
E   TypeError: test_dummy_pool_starmap_with_args.<locals>.multiply() takes 2 positional arguments but 3 were given

flutes/flutes/multiproc.py:95: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_1.py::test_dummy_pool_starmap_with_args
============================== 1 failed in 0.10s ===============================
"""