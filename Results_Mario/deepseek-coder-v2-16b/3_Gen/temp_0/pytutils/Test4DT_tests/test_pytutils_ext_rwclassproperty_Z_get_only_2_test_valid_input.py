
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_only(cls):
        return sentinel.get_only

# Test case for the get_only method
def test_valid_input():
    assert Z.get_only() == sentinel.get_only
