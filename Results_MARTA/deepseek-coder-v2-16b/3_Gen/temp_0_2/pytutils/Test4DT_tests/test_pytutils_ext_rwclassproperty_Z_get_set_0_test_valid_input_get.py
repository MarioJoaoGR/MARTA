
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_set(cls, value=None):
        if value is None:
            return cls._get_set
        cls._get_set = value

def test_valid_input_get():
    # Test retrieving the current value of _get_set when no input is provided
    assert Z.get_set() == sentinel.nothing
    
    # Test setting and retrieving a new value for _get_set
    Z.get_set(value='new_value')
    assert Z.get_set() == 'new_value'
