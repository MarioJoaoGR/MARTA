
# Module: string_utils.generation
# test_string_utils.py
from string_utils import roman_range, roman_encode
import pytest

def test_roman_range_default():
    expected = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    result = list(roman_range(7))
    assert result == expected

def test_roman_range_start_stop():
    expected = ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
    result = list(roman_range(start=7, stop=1, step=-1))