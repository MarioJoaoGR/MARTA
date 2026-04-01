
import pytest
from multiprocessing import Pool, TimeoutError
from flutes.multiproc import safe_pool

def test_valid_input():
    def square(x):
        return x * x
    
    # Test with default parameters
    with safe_pool() as pool:
        results = pool.map(square, range(10))
        assert results == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    
    # Test with specified number of processes
    with safe_pool(processes=4) as pool:
        results = pool.map(square, range(10))
        assert results == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    
    # Test with state_class and init_args
    class PoolState:
        def __init__(self):
            self.data = []
    
    pool_state = PoolState()
    
    with safe_pool(processes=2, state_class=PoolState) as pool:
        results = pool.map(square, range(10))
        assert results == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
        assert pool_state.data == []
    
    # Test with closing and suppress_exceptions
    def closeable():
        pass
    
    closeable.__exit__ = lambda *args: None
    
    with safe_pool(processes=2, closing=[closeable()], suppress_exceptions=True) as pool:
        results = pool.map(square, range(10))
        assert results == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    
    # Test with invalid state_class
    with pytest.raises(ValueError):
        with safe_pool(state_class=int) as pool:
            pass
    
    # Test with invalid closing parameter
    with pytest.raises(ValueError):
        with safe_pool(closing="invalid") as pool:
            pass

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

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        def square(x):
            return x * x
    
        # Test with default parameters
>       with safe_pool() as pool:

flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_valid_input.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/contextlib.py:301: in helper
    return _GeneratorContextManager(func, args, kwds)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <contextlib._GeneratorContextManager object at 0x7fbde445ead0>
func = <function safe_pool at 0x7fbde44eade0>, args = (), kwds = {}

    def __init__(self, func, args, kwds):
>       self.gen = func(*args, **kwds)
E       TypeError: safe_pool() missing 1 required positional argument: 'processes'

/usr/local/lib/python3.11/contextlib.py:105: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.09s ===============================
"""