
import pytest
from string_utils.generation import roman_range

def test_roman_range_valid_sequence():
    expected_output = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    result = list(roman_range(7))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_roman_range_valid_sequence_reverse():
    expected_output = ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
    result = list(roman_range(start=7, stop=1, step=-1))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"

def test_roman_range_valid_sequence_with_step():
    expected_output = ['II', 'IV', 'VI', 'VIII', 'X']
    result = list(roman_range(stop=10, start=2, step=2))
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
