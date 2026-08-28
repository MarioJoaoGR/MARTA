
import pytest
from unittest.mock import patch
import time

# Assuming the wrapper function is defined as per the provided docstring and usage examples.
def wrapper(f):
    def retried(*args, **kwargs):
        retry_count = 0
        if 'retries' in kwargs:
            retries = kwargs['retries']
        else:
            retries = None
        if 'retry_pause' in kwargs:
            retry_pause = kwargs['retry_pause']
        else:
            retry_pause = 1
        ret = None
        while True:
            retry_count += 1
            if retry_count > (retries or float('inf')):
                raise Exception("Retry limit exceeded")
            try:
                ret = f(*args, **kwargs)
            except Exception:
                pass
            if ret:
                break
            time.sleep(retry_pause)
        return ret
    return retried

# Test scenarios
def test_valid_inputs():
    @wrapper
    def example_function():
        return "success"
    
    wrapped_function = example_function()
    assert wrapped_function == "success"

def test_edge_cases():
    @wrapper(retries=None, retry_pause=0)
    def example_function():
        return "success"
    
    with pytest.raises(Exception):
        wrapped_function = example_function()

def test_invalid_inputs():
    with pytest.raises(TypeError):
        @wrapper
        def non_callable_function():
            pass

# Running the tests
if __name__ == "__main__":
    pytest.main()
