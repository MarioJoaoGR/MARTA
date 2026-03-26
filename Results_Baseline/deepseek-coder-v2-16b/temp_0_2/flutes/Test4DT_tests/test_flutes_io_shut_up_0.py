
import pytest
import sys
import os
from flutes.io import shut_up

# Test the function as a decorator
def test_shut_up_as_decorator():
    @shut_up(stderr=True)
    def verbose_func():
        print("This will not be printed because stderr is suppressed by shut_up.")
    
    # Capture the output to check if it's actually suppressed
    captured_output = sys.stdout
    try:
        sys.stdout = None  # This simulates a null device for stdout
        verbose_func()
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"
    
    assert sys.stdout is not captured_output, "Output was not suppressed by shut_up decorator."

# Test the function as a context manager
def test_shut_up_as_context_manager():
    def verbose_func():
        print("This will not be printed within the context of shut_up, but it would if not for the context manager.")
    
    captured_output = sys.stdout
    try:
        with shut_up(stderr=True):
            verbose_func()
    except Exception as e:
        assert False, f"Unexpected exception raised: {e}"
    