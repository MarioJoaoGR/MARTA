
import pytest
from pysnooper.utils import get_shortish_repr



def test_custom_representation_for_integers():
    def custom_repr_int(x):
        return f"Integer: {x}"
    
    conditions = [(int, custom_repr_int)]
    item = 42
    expected_output = 'Integer: 42'
    assert get_shortish_repr(item, custom_repr=conditions) == expected_output


def test_handling_faulty_representation():
    class FaultyObject:
        def __repr__(self):
            raise ValueError("Failed to represent")
    
    faulty_obj = FaultyObject()
    expected_output = 'REPR FAILED'
    assert get_shortish_repr(faulty_obj) == expected_output