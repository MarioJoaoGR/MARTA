
import pytest
from pysnooper.variables import Attrs

class Example:
    __slots__ = ('x', 'y')
    
    def __init__(self):
        self.x = 10
        self.y = 20

class AnotherExample:
    def __init__(self):
        self.a = 30
        self.b = 40

class MixedExample:
    __slots__ = ('x',)
    
    def __init__(self):
        self.x = 10
        self.__dict__['y'] = 20

class SimpleObject:
    pass





def test_invalid_input_none():
    with pytest.raises(TypeError):
        attrs_instance = Attrs()
        keys = list(attrs_instance._keys(None))