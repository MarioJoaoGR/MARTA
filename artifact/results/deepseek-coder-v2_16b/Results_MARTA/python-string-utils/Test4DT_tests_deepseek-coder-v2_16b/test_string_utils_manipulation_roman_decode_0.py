
import pytest
from string_utils.manipulation import __RomanNumbers

def roman_decode(input_string: str) -> int:
    """
    Decode a Roman numeral string into an integer if the provided string is valid.
    
    This function takes a Roman numeral string as input and returns its corresponding integer value. It relies on the `__RomanNumbers` class's `decode` method to perform the conversion, which includes validation of the input string.
    
    *Examples:*
    
    - Valid conversion:
      ```python
      >>> roman_decode('VII')  # returns 7
      ```
    
    - Invalid input (empty string or invalid characters):
      ```python
      >>> roman_decode('')  # Raises ValueError because the input is empty
      >>> roman_decode('ABCD')  # Raises ValueError because the input contains invalid characters
      ```
    
    *Parameters:*
    
    - `input_string` (str): The Roman numeral string to be decoded. It must be a non-empty string containing valid Roman numeral characters ('I', 'V', 'X', etc.).
    
    *Returns:*
    
    - An integer representing the value of the input Roman numeral string.
    
    *Raises:*
    
    - `ValueError`: If the provided `input_string` is empty or contains invalid characters for a Roman numeral.
    
    *Usage:*
    
    To use this function, simply call it with a valid Roman numeral string:
    
    ```python
    print(roman_decode('VII'))  # Output will be 7
    ```
    """
    return __RomanNumbers.decode(input_string)

# Test cases for the roman_decode function
def test_valid_roman_numeral():
    input_string = 'VII'
    assert roman_decode(input_string) == 7, f"Expected 7 for input '{input_string}', but got {roman_decode(input_string)}"

def test_empty_string():
    input_string = ''
    with pytest.raises(ValueError):
        roman_decode(input_string)

def test_invalid_characters():
    input_string = 'ABCD'
    with pytest.raises(ValueError):
        roman_decode(input_string)
