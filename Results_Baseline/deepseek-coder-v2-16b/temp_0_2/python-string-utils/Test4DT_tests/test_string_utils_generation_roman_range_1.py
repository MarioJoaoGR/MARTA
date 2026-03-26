
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
    assert result == expected

def test_roman_range_invalid_step():
    with pytest.raises(ValueError):
        list(roman_range(stop=8, start=1, step=0))  # Invalid step value

def test_roman_range_non_integer_arguments():
    with pytest.raises(ValueError):
        list(roman_range(stop='eight', start='one', step='negative one'))  # Non-integer arguments

def test_roman_range_out_of_bounds():
    with pytest.raises(ValueError):
        list(roman_range(stop=4000, start=1, step=1))  # Out of bounds stop value
    with pytest.raises(ValueError):
        list(roman_range(stop=3999, start=0, step=1))  # Out of bounds start value
    with pytest.raises(ValueError):
        list(roman_range(stop=3999, start=1, step=-4000))  # Out of bounds negative step value

def test_roman_range_invalid_configuration():
    with pytest.raises(OverflowError):
        list(roman_range(stop=2, start=5, step=1))  # Invalid configuration (forward)
    with pytest.raises(OverflowError):
        list(roman_range(stop=5, start=2, step=-1))  # Invalid configuration (backward)

def test_roman_range_zero_step():
    with pytest.raises(ValueError):
        list(roman_range(stop=8, start=1, step=0))  # Zero step value
