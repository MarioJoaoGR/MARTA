
import pytest
from string_utils import roman_range

# Test scenario 1: Test standard input for roman_range function with default values and valid range.
def test_valid_input_standard():
    generator = roman_range(7)
    expected_output = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    assert list(generator) == expected_output

# Test scenario 2: Test standard input for roman_range function with custom start value and default step.
def test_valid_input_custom_start():
    generator = roman_range(stop=7, start=2)
    expected_output = ['II', 'III', 'IV', 'V', 'VI', 'VII']
    assert list(generator) == expected_output

# Test scenario 3: Test raising ValueError for invalid input values such as negative numbers or out of range.
def test_invalid_input():
    with pytest.raises(ValueError):
        generator = roman_range(stop=-1, start=1)
