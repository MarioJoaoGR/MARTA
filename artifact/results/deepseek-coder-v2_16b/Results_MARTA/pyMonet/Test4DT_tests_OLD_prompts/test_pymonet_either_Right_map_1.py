
import pytest
from pymonet.either import Right, Left

def test_valid_input():
    right_value = Right(42)
    mapped_right = right_value.map(lambda x: x * 2)
    assert isinstance(mapped_right, Right)
    assert mapped_right.value == 84

def test_invalid_input():
    with pytest.raises(TypeError):
        Right().map(lambda x: x)
