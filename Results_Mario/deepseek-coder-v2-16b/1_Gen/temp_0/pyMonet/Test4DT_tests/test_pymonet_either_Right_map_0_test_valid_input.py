
import pytest
from pymonet.either import Right

def test_valid_input():
    right_value = Right(42)
    assert right_value.value == 42
