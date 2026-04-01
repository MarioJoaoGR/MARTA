
from typing import Union
import pytest
from string_utils.manipulation import roman_encode

def test_valid_string():
    assert roman_encode("37") == 'XXXVII'
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode("2020") == 'MMXX'
    assert roman_encode(2020) == 'MMXX'
