
from string_utils.generation import roman_range
import pytest

def test_valid_input_happy_path():
    # Test generating Roman numerals from 1 to 7
    result = list(roman_range(7))
    assert result == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    # Test generating Roman numerals from 7 down to 1
    result = list(roman_range(start=7, stop=1, step=-1))
    assert result == ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']

    # Test generating Roman numerals with custom start and step
    result = list(roman_range(start=2, stop=8, step=2))
    assert result == ['II', 'IV', 'VI', 'VIII']

    # Test generating Roman numerals with negative step
    result = list(roman_range(start=10, stop=4, step=-2))
    assert result == ['X', 'VIII', 'VI', 'IV']
