
import pytest
from pytutils.ext.rwclassproperty import sentinel

# Assuming the following code for Z and get_set is provided in the setup section
class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_set(cls):
        return cls._get_set

def test_get_current_value():
    # Test getting the current value when it is not set
    assert Z.get_set() == sentinel.nothing

    # Test setting a new value and then retrieving it
    Z._get_set = 'new_value'
    assert Z.get_set() == 'new_value'
