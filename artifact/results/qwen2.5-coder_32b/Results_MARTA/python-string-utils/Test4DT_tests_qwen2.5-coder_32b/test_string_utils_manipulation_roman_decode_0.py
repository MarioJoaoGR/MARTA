
import pytest
from string_utils.manipulation import roman_decode

def test_roman_decode_basic():
    assert roman_decode('VII') == 7
