
from string_utils.generation import roman_range  # Assuming this is the correct module path
import pytest

def test_valid_case():
    expected_output = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    
    gen = roman_range(7)
    result = [next(gen) for _ in range(len(expected_output))]
    assert result == expected_output

def test_valid_case_reverse():
    expected_output = ['VII', 'VI', 'V', 'IV', 'III', 'II', 'I']
    
    gen = roman_range(start=7, stop=1, step=-1)
    result = [next(gen) for _ in range(len(expected_output))]
    assert result == expected_output
