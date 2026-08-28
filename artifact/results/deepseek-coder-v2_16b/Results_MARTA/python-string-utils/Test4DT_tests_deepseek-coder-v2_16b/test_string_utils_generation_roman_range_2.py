
import pytest
from string_utils.generation import roman_range

def test_valid_roman_range():
    # Test generating a sequence from 1 to 7
    result = list(roman_range(7))
    assert result == ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']


def test_negative_step_valid_range():
    # Test generating a sequence from 5 to 3 with a negative step
    result = list(roman_range(start=5, stop=3, step=-1))
    assert result == ['V', 'IV', 'III']