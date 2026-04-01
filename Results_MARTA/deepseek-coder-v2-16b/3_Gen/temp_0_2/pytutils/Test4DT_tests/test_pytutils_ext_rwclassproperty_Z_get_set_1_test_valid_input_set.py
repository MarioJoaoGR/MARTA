
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
    # Initial state should be sentinel.nothing
    assert Z.get_set() == sentinel.nothing
    
    # Set a new value and check if it is set correctly
    Z.get_set(value='new_value')
    assert Z._get_set == 'new_value'
    
    # Retrieve the value to ensure it remains unchanged
    assert Z.get_set() == 'new_value'
