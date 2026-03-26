
import pytest
from pytutils.excs import ok

def test_valid_inputs():
    with ok(ZeroDivisionError):
        assert 1 / 0 == float('inf')  # This should pass silently without raising an error.
