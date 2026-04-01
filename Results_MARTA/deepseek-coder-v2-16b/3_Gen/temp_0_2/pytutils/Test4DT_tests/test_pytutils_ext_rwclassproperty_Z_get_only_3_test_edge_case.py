
from pytutils.ext.rwclassproperty import sentinel
import pytest

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_only(cls):
        return sentinel.get_only

# Test Case for the get_only method
def test_get_only():
    assert Z.get_only() == sentinel.get_only
