
import pytest
from pymonet.either import Right, Left

# Test valid input where Right is not empty and has a valid value
def test_valid_input():
    right_instance = Right('string')
    assert isinstance(right_instance.map(lambda x: len(x)), Right)
    assert right_instance.map(lambda x: len(x)).value == 6

# Test invalid input where the expected exception is not raised
def test_invalid_input():
    with pytest.raises(TypeError):
        Right()
