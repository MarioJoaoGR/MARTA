
import multiprocessing as mp
from flutes.multiproc import Proxy, Event, NewEvent, get_worker_id

class TestProxyNewInvalidInput:
    def test_invalid_input(self):
        queue = mp.Queue()
        proxy = Proxy(queue)
        
        # Test with None iterable and invalid update_frequency (negative integer)
        try:
            result = proxy.new(iterable=None, update_frequency=-5)
            assert False, "Expected ValueError for negative update_frequency"
        except ValueError as e:
            assert str(e) == "`update_frequency` must be positive", f"Unexpected error message: {str(e)}"
        
        # Test with None iterable and invalid update_frequency (zero)
        try:
            result = proxy.new(iterable=None, update_frequency=0)
            assert False, "Expected ValueError for zero update_frequency"
        except ValueError as e:
            assert str(e) == "`update_frequency` must be positive", f"Unexpected error message: {str(e)}"
        
        # Test with None iterable and invalid update_frequency (float not in range 0-1)
        try:
            result = proxy.new(iterable=None, update_frequency=1.5)
            assert False, "Expected ValueError for float update_frequency out of range"
        except ValueError as e:
            assert str(e) == "`update_frequency` must be within the range (0, 1]", f"Unexpected error message: {str(e)}"
        
        # Test with iterable and invalid update_frequency (float not in range 0-1 even with valid length)
        iterable = [1, 2, 3]
        try:
            result = proxy.new(iterable=iterable, update_frequency=1.5)
            assert False, "Expected ValueError for float update_frequency out of range"
        except ValueError as e:
            assert str(e) == "`update_frequency` must be within the range (0, 1]", f"Unexpected error message: {str(e)}"
        
        # Test with iterable and invalid update_frequency (negative integer)
        try:
            result = proxy.new(iterable=iterable, update_frequency=-5)
            assert False, "Expected ValueError for negative update_frequency"
        except ValueError as e:
            assert str(e) == "`update_frequency` must be positive", f"Unexpected error message: {str(e)}"
        
        # Test with iterable and invalid update_frequency (zero)
        try:
            result = proxy.new(iterable=iterable, update_frequency=0)
            assert False, "Expected ValueError for zero update_frequency"
        except ValueError as e:
            assert str(e) == "`update_frequency` must be positive", f"Unexpected error message: {str(e)}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_Proxy_new_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_Proxy_new_0_test_invalid_input.py:3:0: E0611: No name 'Proxy' in module 'flutes.multiproc' (no-name-in-module)


"""