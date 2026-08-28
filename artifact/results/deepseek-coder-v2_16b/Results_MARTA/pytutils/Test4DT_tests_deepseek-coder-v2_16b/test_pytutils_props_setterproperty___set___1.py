
import pytest
from pytutils.props import setterproperty


def test_set_value():
    class MyClass:
        def __init__(self, initial):
            self._value = None
    
        @setterproperty
        def value(self, new_value):
            self._value = new_value
    
    obj = MyClass(10)
    assert obj._value is None
    obj.value = 20
    assert obj._value == 20
