
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_only(cls):
        return sentinel.get_only

# Test case to check the edge case where only a class method is used
def test_edge_case():
    result = Z.get_only()
    assert result == sentinel.get_only
