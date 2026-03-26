
from string_utils.manipulation import roman_encode  # Assuming the module is correctly imported
import pytest

def test_roman_encode():
    assert roman_encode(37) == 'XXXVII'
    assert roman_encode('2020') == 'MMXX'
