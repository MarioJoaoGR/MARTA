
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    def get_only(self):
        return sentinel.get_only

# Test case for error scenario
def test_error_case():
    z = Z()
    assert z.get_only() == sentinel.get_only
