
import pytest
from pytutils.excs import ok

def test_valid_case_no_exceptions():
    with ok():
        # No exceptions should be raised within this block
        assert True
