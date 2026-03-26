
import pytest
from pymonet.either import Right

def test_valid_input():
    right_value = Right(42)
    assert right_value.value == 42
    mapped_value = right_value.map(lambda x: x * 2)
    assert isinstance(mapped_value, Right)
    assert mapped_value.value == 84
