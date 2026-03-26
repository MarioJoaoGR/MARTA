
import pytest
from pytutils.ext.rwclassproperty import sentinel

# Assuming the class Z and its method get_set are defined as per the provided setup and function code.
class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_set(cls, value=None):
        if value is None:
            return cls._get_set
        cls._get_set = value

def test_valid_input_get():
    # Initial state should be sentinel.nothing
    assert Z.get_set() == sentinel.nothing
    
    # Set a new value and check if it is correctly set
    new_value = object()
    Z.get_set(new_value)
    assert Z._get_set == new_value
    
    # Retrieve the value again to ensure it remains unchanged
    retrieved_value = Z.get_set()
    assert retrieved_value == new_value
