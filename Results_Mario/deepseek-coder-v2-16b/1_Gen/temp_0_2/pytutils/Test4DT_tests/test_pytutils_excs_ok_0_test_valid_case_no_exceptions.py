
import pytest
from pytutils.excs import ok

def test_valid_case_no_exceptions():
    with ok():
        assert 1 + 1 == 2
