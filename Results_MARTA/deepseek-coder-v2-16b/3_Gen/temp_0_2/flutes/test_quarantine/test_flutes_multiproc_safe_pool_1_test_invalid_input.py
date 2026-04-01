
import contextlib
from multiprocessing import Pool, DummyPool
from flutes.multiproc import safe_pool, PoolState

def test_invalid_input():
    # Test case for invalid input where state_class is not a subclass of PoolState
    try:
        with safe_pool(processes=4, state_class=int) as pool:  # Invalid state_class
            assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "`state_class` must be a subclass of `flutes.PoolState`"

    # Test case for invalid input where closing is not a list
    try:
        with safe_pool(processes=4, closing="not a list") as pool:  # Invalid closing
            assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "`closing` should either be `None` or a list"

    # Test case for invalid input where an object in closing is not callable or has no close method
    class NonCallableObject:
        pass
    
    try:
        with safe_pool(processes=4, closing=[NonCallableObject()]) as pool:  # Invalid object in closing
            assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "Invalid object in `closing` list. The object must either be a callable or has a `close` method"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_safe_pool_1_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_safe_pool_1_test_invalid_input.py:3:0: E0611: No name 'DummyPool' in module 'multiprocessing' (no-name-in-module)


"""