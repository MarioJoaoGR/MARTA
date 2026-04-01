
import pytest
from pymonet.either import Right

def test_valid_input():
    right_instance = Right(42)
    mapped_value = right_instance.bind(lambda x: x * 2)
    assert mapped_value == 84
