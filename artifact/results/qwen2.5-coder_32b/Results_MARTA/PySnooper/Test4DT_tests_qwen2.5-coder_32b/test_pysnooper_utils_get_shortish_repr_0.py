
import pytest
from pysnooper.utils import get_shortish_repr



def test_custom_representation():
    def custom_repr_int(x):
        return f"Integer: {x}"
    conditions = [(int, custom_repr_int)]
    result = get_shortish_repr(42, custom_repr=conditions)
    assert result == 'Integer: 42'

def test_no_truncation():
    result = get_shortish_repr([1, 2, 3], custom_repr=[], max_length=None, normalize=False)
    assert result == '[1, 2, 3]'

def test_exception_handling():
    class FaultyObject:
        def __repr__(self):
            raise ValueError("Failed to represent")
    faulty_obj = FaultyObject()
    result = get_shortish_repr(faulty_obj)
    assert result == 'REPR FAILED'


def test_callable_condition():
    def is_even(x):
        return isinstance(x, int) and x % 2 == 0
    def even_repr(x):
        return f"Even number: {x}"
    conditions = [(is_even, even_repr)]
    result = get_shortish_repr(4, custom_repr=conditions)
    assert result == 'Even number: 4'