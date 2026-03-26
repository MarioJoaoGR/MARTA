
import pytest
import subprocess
from flutes.run import error_wrapper

def test_invalid_inputs():
    # Test that non-subprocess errors are returned unchanged
    err = ValueError("Test error")
    wrapped_error = error_wrapper(err)
    assert str(wrapped_error) == "Test error"
    
    # Test that subprocess errors are wrapped with captured output
    try:
        result = subprocess.run(['false'], capture_output=True, text=True)
    except Exception as e:
        wrapped_error = error_wrapper(e)
        assert str(wrapped_error).startswith("Captured output:\n")
