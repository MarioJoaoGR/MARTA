
import os
from contextlib import contextmanager
import pytest

def chdir(path: str) -> Iterator[None]:
    """Context manager for changing dir and restoring previous workdir after exit."""
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

@contextmanager
def test_chdir():
    with pytest.raises(FileNotFoundError):
        with chdir("invalid/path"):
            pass

# To run the test, you would call the function directly or integrate it into a larger test suite.

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_chdir_0_test_invalid_input
isort/Test4DT_tests/test_isort_deprecated_finders_chdir_0_test_invalid_input.py:6:24: E0602: Undefined variable 'Iterator' (undefined-variable)


"""