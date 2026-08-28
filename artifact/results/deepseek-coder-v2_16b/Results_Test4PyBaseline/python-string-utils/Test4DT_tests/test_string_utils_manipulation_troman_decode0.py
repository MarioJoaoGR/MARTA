# Module: string_utils.manipulation
# test_string_utils.py
from string_utils.manipulation import roman_decode

def test_roman_decode_valid_VII():
    assert roman_decode('VII') == 7, "Test failed for input 'VII'"

def test_roman_decode_valid_XIV():
    assert roman_decode('XIV') == 14, "Test failed for input 'XIV'"

def test_roman_decode_valid_MCMXCIV():
    assert roman_decode('MCMXCIV') == 1994, "Test failed for input 'MCMXCIV'"

# Additional edge cases can be added to ensure robustness
