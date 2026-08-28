
import pytest
from pysnooper.utils import get_shortish_repr

def test_basic_list_representation():
    assert get_shortish_repr([1, 2, 3]) == '[1, 2, 3]'

def test_custom_representation_for_integers():
    def custom_repr_int(x):
        return f"Integer: {x}"
    conditions = [(int, custom_repr_int)]
    assert get_shortish_repr(42, custom_repr=conditions) == 'Integer: 42'




def test_custom_representation_with_callable_condition():
    def is_even(x):
        return isinstance(x, int) and x % 2 == 0
    def even_repr(x):
        return f"Even number: {x}"
    conditions = [(is_even, even_repr)]
    assert get_shortish_repr(4, custom_repr=conditions) == 'Even number: 4'

def test_handling_exception_in_representation():
    class FaultyObject:
        def __repr__(self):
            raise ValueError("Failed to represent")
    faulty_obj = FaultyObject()
    assert get_shortish_repr(faulty_obj) == 'REPR FAILED'