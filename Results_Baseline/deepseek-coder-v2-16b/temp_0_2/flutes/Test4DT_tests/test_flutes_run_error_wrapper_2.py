
import subprocess
from subprocess import CalledProcessError, TimeoutExpired
import pytest

# Import the function correctly using its module name
from flutes.run import error_wrapper

def test_error_wrapper_with_unicode_output():
    # Simulate a command that generates Unicode output
    try:
        result = subprocess.run(['python', '-c', 'print("a"*1000)'], capture_output=True, text='utf-8')
    except CalledProcessError as err:
        err = error_wrapper(err)
        assert "Captured output:" in str(err), "Expected captured output to be included in the string representation."
        assert len(str(err).split('\n')[2]) <= 79, "Output lines should not exceed 80 characters as per typical terminal width."

def test_error_wrapper_without_output():
    # Simulate a command that does not generate any output
    try:
        result = subprocess.run(['true'], capture_output=True, text=True)
    except CalledProcessError as err:
        err = error_wrapper(err)
        assert "No output was generated." in str(err), "Expected a message indicating no output when there is none."

def test_error_wrapper_with_non_subprocess_exception():
    # Simulate an exception that is not a subprocess error
    class NonSubprocessError(Exception):
        pass
    
    err = NonSubprocessError("Test non-subprocess error")
    wrapped_err = error_wrapper(err)
    assert isinstance(wrapped_err, type(err)), "Expected the same exception type to be returned."
    assert str(wrapped_err) == str(err), "The string representation of the original and wrapped errors should match."
