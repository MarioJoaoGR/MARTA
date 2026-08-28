
import itertools
import pytest

class Attrs:
    def _keys(self, main_value):
        return itertools.chain(
            getattr(main_value, '__dict__', {}).keys(),
            getattr(main_value, '__slots__', ()))

# Test cases
def test_valid_case_with_slots():
    class Example:
        __slots__ = ('x', 'y')
        
        def __init__(self):
            self.x = 10
            self.y = 20

    obj = Example()
    attrs_instance = Attrs()
    keys = list(attrs_instance._keys(obj))
    assert keys == ['x', 'y']

def test_valid_case_with_dict():
    class AnotherExample:
        def __init__(self):
            self.a = 30
            self.b = 40

    another_obj = AnotherExample()
    attrs_instance = Attrs()
    keys = list(attrs_instance._keys(another_obj))
    assert keys == ['a', 'b']

def test_invalid_input_none():
    attrs_instance = Attrs()
    keys = list(attrs_instance._keys(None))
    assert keys == []
