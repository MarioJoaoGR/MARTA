
import pytest
from unittest.mock import patch
from pytutils.props import setterproperty

class MyClass:
    def __init__(self, value):
        self._value = value
    
    @setterproperty
    def value(self, new_value):
        if not isinstance(new_value, int): raise ValueError('Must be an integer')

def test_invalid_input():
    with pytest.raises(ValueError) as excinfo:
        obj = MyClass(10)
        obj.value = "not an integer"  # This should trigger the setter property's validation
    
    assert str(excinfo.value) == 'Must be an integer'
