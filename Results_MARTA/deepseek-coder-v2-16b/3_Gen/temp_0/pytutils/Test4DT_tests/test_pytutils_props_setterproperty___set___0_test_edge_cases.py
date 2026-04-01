
import pytest
from pytutils.props import setterproperty

class MyClass:
    def __init__(self, initial_value):
        self._value = initial_value
    
    @setterproperty
    def value(self, new_value):
        self._value = new_value
    
    def get_value(self):
        return self._value

def test_setterproperty():
    obj = MyClass(10)
    assert obj.get_value() == 10
    obj.value = 20
    assert obj.get_value() == 20
