
import pytest
from string_utils.manipulation import roman_decode

def test_roman_decode_simple():
    assert roman_decode('I') == 1
    assert roman_decode('V') == 5
    assert roman_decode('X') == 10
    assert roman_decode('L') == 50
    assert roman_decode('C') == 100
    assert roman_decode('D') == 500