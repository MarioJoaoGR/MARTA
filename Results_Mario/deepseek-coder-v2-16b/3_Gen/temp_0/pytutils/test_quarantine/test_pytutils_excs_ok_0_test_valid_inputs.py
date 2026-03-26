
import pytest
from pytutils.excs import ok

def test_valid_inputs():
    # Test passing through ZeroDivisionError
    try:
        with ok(ZeroDivisionError):
            assert 1 / 0 == float('inf')  # This should not raise an error because ZeroDivisionError is passed.
    except ZeroDivisionError:
        pytest.fail("Expected no exception, got ZeroDivisionError")
    
    # Test passing through ValueError
    try:
        with ok(ValueError):
            raise ValueError("Test exception")  # This should not raise an error because ValueError is passed.
    except ValueError as e:
        assert str(e) == "Test exception"
    
    # Test no exceptions, everything should pass through normally
    try:
        with ok():
            x = 1 / 0  # This would normally raise ZeroDivisionError
            raise ValueError("Another test exception")  # This would normally raise ValueError
    except Exception as e:
        pytest.fail(f"Unexpected exception caught: {e}")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
ERROR: usage: __main__.py [options] [file_or_dir] [file_or_dir] [...]
__main__.py: error: unrecognized arguments: --cov=pytutils --cov-report=term --cov-branch --no-cov-on-fail
  inifile: /projects/F202407648IACDCF2/mario/pytutils/pytest.ini
  rootdir: /projects/F202407648IACDCF2/mario/pytutils
"""