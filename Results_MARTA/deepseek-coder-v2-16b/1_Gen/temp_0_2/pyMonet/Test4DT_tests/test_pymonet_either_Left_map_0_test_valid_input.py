
import pytest
from pymonet.either import Left

def test_valid_input():
    left_value = Left("valid_string")
    assert isinstance(left_value, Left)
    assert left_value.map(lambda x: x) == Left("valid_string")
