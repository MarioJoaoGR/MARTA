
from pytutils.ext.rwclassproperty import sentinel
import pytest

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_only(cls):
        return cls._get_set

# Test Case for the edge case scenario
def test_edge_case():
    assert Z.get_only() == sentinel.nothing
