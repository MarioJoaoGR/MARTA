
import pytest
from unittest.mock import patch
from string_utils.manipulation import roman_encode

# Test valid input as integer
def test_valid_input_integer():
    with patch('string_utils.manipulation.__RomanNumbers.encode') as mock_encode:
        mock_encode.return_value = 'XXXVIII'
        assert roman_encode(37) == 'XXXVIII'

# Test valid input as string
def test_valid_input_string():
    with patch('string_utils.manipulation.__RomanNumbers.encode') as mock_encode:
        mock_encode.return_value = 'MMXX'
        assert roman_encode('2020') == 'MMXX'

# Test invalid input, should raise ValueError
def test_invalid_input():
    with pytest.raises(ValueError):
        roman_encode(-1)
        roman_encode(4000)
