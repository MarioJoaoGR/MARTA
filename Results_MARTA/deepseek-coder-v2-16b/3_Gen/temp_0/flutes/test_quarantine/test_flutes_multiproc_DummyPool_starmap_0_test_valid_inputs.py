
import pytest
from multiprocessing import Pool, cpu_count
from typing import Optional, Callable, Iterable, Any, List, Tuple
from flutes.multiproc import DummyPool

@pytest.fixture(scope="module")
def dummy_pool():
    return DummyPool(processes=0)

def test_valid_inputs(dummy_pool):
    def func(a, b):
        return a + b
    
    inputs = [(1, 2), (3, 4)]
    results = dummy_pool.starmap(func, inputs)
    
    assert len(results) == len(inputs)
    for result in results:
        assert isinstance(result, int)
        assert result == sum(t[0] + t[1] for t in inputs if (t[0], t[1]) == tuple(result))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

dummy_pool = <flutes.multiproc.DummyPool object at 0x7f3e77a59610>

    def test_valid_inputs(dummy_pool):
        def func(a, b):
            return a + b
    
        inputs = [(1, 2), (3, 4)]
        results = dummy_pool.starmap(func, inputs)
    
        assert len(results) == len(inputs)
        for result in results:
            assert isinstance(result, int)
>           assert result == sum(t[0] + t[1] for t in inputs if (t[0], t[1]) == tuple(result))

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_0_test_valid_inputs.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f3e769c9a20>

>   assert result == sum(t[0] + t[1] for t in inputs if (t[0], t[1]) == tuple(result))
E   TypeError: 'int' object is not iterable

flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_0_test_valid_inputs.py:21: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_DummyPool_starmap_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================

"""