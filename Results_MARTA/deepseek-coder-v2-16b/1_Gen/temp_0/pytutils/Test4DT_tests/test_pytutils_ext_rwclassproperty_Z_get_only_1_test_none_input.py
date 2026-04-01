
from pytutils.ext.rwclassproperty import sentinel
import pytest

def get_only(cls):
    return sentinel.get_only

# Test case to check if get_only returns the expected value when no input is provided
def test_none_input():
    class Z:
        _get_set = sentinel.nothing
    
    z_instance = Z()
    assert get_only(Z) == sentinel.get_only
