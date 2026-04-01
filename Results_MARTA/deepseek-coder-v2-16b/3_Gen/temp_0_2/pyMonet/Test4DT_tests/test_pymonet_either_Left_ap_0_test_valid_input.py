
import pytest
from pymonet.either import Left, Right

def test_valid_input():
    left_value = Left('valid_string')
    assert isinstance(left_value, Left)
    assert left_value.value == 'valid_string'
