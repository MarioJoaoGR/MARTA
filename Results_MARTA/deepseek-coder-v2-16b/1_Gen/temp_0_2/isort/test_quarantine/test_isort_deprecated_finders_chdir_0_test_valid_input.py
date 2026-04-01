
import os
from collections import Iterator

def chdir(path: str) -> Iterator[None]:
    """Context manager for changing dir and restoring previous workdir after exit."""
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_deprecated_finders_chdir_0_test_valid_input
isort/Test4DT_tests/test_isort_deprecated_finders_chdir_0_test_valid_input.py:3:0: E0611: No name 'Iterator' in module 'collections' (no-name-in-module)


"""