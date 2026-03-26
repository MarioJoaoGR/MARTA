
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_set(cls, value=None):
        if value is None:
            return cls._get_set
        cls._get_set = value

def test_valid_input_set():
    # Test setting the _get_set attribute with a valid value
    Z.get_set(value='some_value')
    assert Z._get_set == 'some_value'
    
    # Test retrieving the current value of the _get_set attribute
    assert Z.get_set() == 'some_value'
