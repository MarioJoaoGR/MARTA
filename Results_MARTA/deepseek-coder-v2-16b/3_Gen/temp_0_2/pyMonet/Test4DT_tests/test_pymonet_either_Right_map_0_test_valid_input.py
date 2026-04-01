
import pytest
from pymonet.either import Right

def test_valid_input():
    right_value = Right(42)
    assert right_value.value == 42
    
    def mapper(x):
        return x * 2
    
    mapped_right = right_value.map(mapper)
    assert isinstance(mapped_right, Right)
    assert mapped_right.value == 84
