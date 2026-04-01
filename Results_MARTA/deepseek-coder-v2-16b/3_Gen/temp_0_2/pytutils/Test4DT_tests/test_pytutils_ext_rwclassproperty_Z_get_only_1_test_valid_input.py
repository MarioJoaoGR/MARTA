
from pytutils.ext.rwclassproperty import sentinel
import pytest

class Z:
    _get_set = sentinel.nothing
    
    def get_only(self):
        return sentinel.get_only

# Test case for valid input
def test_valid_input():
    z = Z()
    assert z.get_only() == sentinel.get_only
