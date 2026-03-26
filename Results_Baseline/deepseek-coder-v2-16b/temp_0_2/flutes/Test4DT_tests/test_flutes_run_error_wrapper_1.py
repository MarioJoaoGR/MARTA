
import subprocess
from subprocess import CalledProcessError, TimeoutExpired
import pytest

# Import the function correctly using its module name
from flutes.run import error_wrapper

def test_error_wrapper_with_calledprocesserror():
    try:
        # Simulate a command that raises CalledProcessError
        result = subprocess.run(['false'], capture_output=True, text=True)
    except CalledProcessError as err:
        # Wrap the exception with error_wrapper
        err = error_wrapper(err)
        assert "Captured output:" in str(err), "Expected captured output to be included in the string representation."
        assert "Command 'false' returned non-zero exit status 1" in str(err), "Expected the original error message to remain."

def test_error_wrapper_with_timeoutexpired():
    try:
        # Simulate a command that times out, raising TimeoutExpired
        result = subprocess.run(['sleep', '10'], timeout=1, capture_output=True, text=True)
    except TimeoutExpired as err:
        # Wrap the exception with error_wrapper
        err = error_wrapper(err)