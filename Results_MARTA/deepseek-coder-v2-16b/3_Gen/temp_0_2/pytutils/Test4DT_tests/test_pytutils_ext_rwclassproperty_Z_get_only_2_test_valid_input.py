
import pytest
from pytutils.ext.rwclassproperty import sentinel

class Z:
    _get_set = sentinel.nothing
    
    @classmethod
    def get_only(cls):
        return sentinel.get_only

def test_valid_input():
    # Create an instance of the class
    z_instance = Z()
    
    # Call the get_only method on the instance
    result = z_instance.get_only()
    
    # Assert that the result is 'sentinel.get_only'
    assert result == sentinel.get_only
