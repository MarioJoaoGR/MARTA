
# Module: flutes.multiproc
import pytest
from multiprocessing import PoolState
import contextlib
from flutes.multiproc import safe_pool

# Test cases for safe_pool function

def test_safe_pool_basic_usage():
    class MyPoolState(PoolState):
        def __init__(self):
            self.data = []
    
    with pytest.raises(ValueError, match="`state_class` must be a subclass of `flutes.PoolState`"):
        with safe_pool(processes=4, state_class=MyPoolState) as pool:  # This should raise ValueError
            pass

def test_safe_pool_no_stateful_processes():
    with safe_pool(processes=4) as pool:
        results = pool.map(lambda x: x * 2, range(10))
        assert results == list(range(0, 20, 2)), "Results should be double the input values"

def test_safe_pool_custom_init_args():
    class MyPoolState(PoolState):
        def __init__(self, initial_data):
            self.data = initial_data
    
    with safe_pool(processes=4, state_class=MyPoolState, init_args=(['initial data'],)) as pool:
        results = pool.map(lambda x: x * 2, range(10))
        assert results == list(range(0, 20, 2)), "Results should be double the input values"

def test_safe_pool_closing_routines():
    def close_routine():
        print("Closing routine called")
    
    with pytest.raises(ValueError, match="Invalid object in `closing` list."):
        with safe_pool(processes=4, closing=[close_routine]) as pool:  # This should raise ValueError
            pass

def test_safe_pool_suppress_exceptions():
    with safe_pool(processes=4, suppress_exceptions=True) as pool:
        results = pool.map(lambda x: x * 2, range(10))
        assert results == list(range(0, 20, 2)), "Results should be double the input values"

if __name__ == "__main__":
    pytest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_0
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_0.py:4:0: E0611: No name 'PoolState' in module 'multiprocessing' (no-name-in-module)


"""